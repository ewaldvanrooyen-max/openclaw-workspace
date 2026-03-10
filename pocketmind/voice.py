#!/usr/bin/env python3
"""
PocketMind Voice Module

Provides speech-to-text (voice input) and text-to-speech (voice output)
capabilities for PocketMind.

Voice Input:
    - Uses OpenAI Whisper (via openai-whisper package)
    - Uses tiny model by default for speed
    - Records audio from microphone

Voice Output:
    - Uses Edge TTS (edge-tts package) for high-quality offline TTS
    - Falls back to gtts for simple usage
    - Plays audio through speakers

Usage:
    from voice import VoiceInput, VoiceOutput
    
    # For voice input
    voice_in = VoiceInput()
    text = voice_in.listen()  # Records and transcribes
    
    # For voice output
    voice_out = VoiceOutput()
    voice_out.speak("Hello, I am PocketMind!")
"""

import os
import sys
import tempfile
import subprocess
import threading
import time

# Try to import required packages
WHISPER_AVAILABLE = False
EDGE_TTS_AVAILABLE = False
SOUNDDEVICE_AVAILABLE = False

try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    pass

try:
    import edge_tts
    EDGE_TTS_AVAILABLE = True
except ImportError:
    pass

try:
    import sounddevice as sd
    import numpy as np
    SOUNDDEVICE_AVAILABLE = True
except ImportError:
    pass


class VoiceInput:
    """
    Speech-to-text voice input handler.
    
    Uses OpenAI Whisper for transcription.
    Records audio from microphone and transcribes it.
    """
    
    def __init__(self, model_size="tiny", device="cpu"):
        """
        Initialize voice input.
        
        Args:
            model_size: Whisper model size (tiny, base, small, medium, large)
            device: Device to use (cpu, cuda)
        """
        self.model_size = model_size
        self.device = device
        self.model = None
        
        if not WHISPER_AVAILABLE:
            raise ImportError(
                "openai-whisper not installed. Install with: pip install openai-whisper"
            )
        
        # Load model
        self._load_model()
    
    def _load_model(self):
        """Load Whisper model."""
        print(f"📥 Loading Whisper model ({self.model_size})...")
        try:
            self.model = whisper.load_model(self.model_size, device=self.device)
            print("✓ Whisper model loaded")
        except Exception as e:
            print(f"⚠ Failed to load Whisper model: {e}")
            raise
    
    def listen(self, timeout=10, phrase_time_limit=30):
        """
        Listen for voice input and transcribe.
        
        Args:
            timeout: Max time to wait for speech to start (seconds)
            phrase_time_limit: Max duration of speech to capture (seconds)
            
        Returns:
            Transcribed text
        """
        if SOUNDDEVICE_AVAILABLE:
            return self._record_and_transcribe(timeout, phrase_time_limit)
        else:
            return self._record_with_subprocess(timeout, phrase_time_limit)
    
    def _record_and_transcribe(self, timeout, phrase_time_limit):
        """Record audio using sounddevice and transcribe."""
        print("🎤 Listening... (speak now)")
        
        # Audio settings
        sample_rate = 16000
        channels = 1
        
        # Record audio
        audio_data = []
        
        def callback(indata, frames, time_info, status):
            if status:
                print(f"⚠ Audio status: {status}")
            audio_data.append(indata.copy())
        
        try:
            with sd.InputStream(
                samplerate=sample_rate,
                channels=channels,
                dtype='float32',
                callback=callback
            ):
                sd.sleep(phrase_time_limit * 1000)
        except Exception as e:
            print(f"⚠ Recording error: {e}")
            return ""
        
        if not audio_data:
            print("⚠ No audio captured")
            return ""
        
        # Concatenate audio
        audio = np.concatenate(audio_data)
        
        # Convert to 16-bit PCM
        audio = (audio * 32767).astype(np.int16)
        
        # Transcribe
        print("🔄 Transcribing...")
        result = self.model.transcribe(audio, fp16=False)
        
        text = result["text"].strip()
        print(f"📝 Transcribed: {text}")
        
        return text
    
    def _record_with_subprocess(self, timeout, phrase_time_limit):
        """Record audio using arecord (Linux) or sox, then transcribe."""
        print("🎤 Recording audio...")
        
        # Create temp file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            temp_file = f.name
        
        try:
            # Try arecord (Linux)
            cmd = [
                "arecord",
                "-f", "CD",           # CD quality
                "-t", "wav",
                "-d", str(phrase_time_limit),
                temp_file
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=phrase_time_limit + 5
            )
            
            if result.returncode != 0:
                # Try rec (sox) as fallback
                cmd = [
                    "rec",
                    "-q",               # Quiet
                    "-r", "16000",
                    "-c", "1",
                    "-t", "wav",
                    temp_file
                ]
                subprocess.run(
                    cmd,
                    capture_output=True,
                    timeout=phrase_time_limit + 5
                )
            
            # Check file
            if not os.path.exists(temp_file) or os.path.getsize(temp_file) == 0:
                print("⚠ No audio recorded")
                return ""
            
            # Transcribe
            print("🔄 Transcribing...")
            result = self.model.transcribe(temp_file, fp16=False)
            
            text = result["text"].strip()
            print(f"📝 Transcribed: {text}")
            
            return text
            
        except FileNotFoundError:
            print("⚠ No audio recording tool found (arecord/rec)")
            print("   Install with: sudo apt install sox")
            return ""
        except subprocess.TimeoutExpired:
            print("⚠ Recording timed out")
            return ""
        except Exception as e:
            print(f"⚠ Recording error: {e}")
            return ""
        finally:
            # Cleanup
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def transcribe_file(self, audio_path):
        """
        Transcribe an audio file.
        
        Args:
            audio_path: Path to audio file
            
        Returns:
            Transcribed text
        """
        if not os.path.exists(audio_path):
            return f"File not found: {audio_path}"
        
        print(f"🔄 Transcribing {audio_path}...")
        result = self.model.transcribe(audio_path, fp16=False)
        
        return result["text"].strip()


class VoiceOutput:
    """
    Text-to-speech voice output handler.
    
    Uses Edge TTS for high-quality speech synthesis.
    Falls back to other TTS engines if needed.
    """
    
    # Default voice for Edge TTS
    DEFAULT_VOICE = "en-US-AriaNeural"
    
    # Available voices
    VOICES = {
        "female": "en-US-AriaNeural",
        "male": "en-US-GuyNeural",
        "british": "en-GB-SoniaNeural",
        "australian": "en-AU-NatashaNeural",
    }
    
    def __init__(self, voice=None, rate="+0%", pitch="+0Hz"):
        """
        Initialize voice output.
        
        Args:
            voice: Voice name (female, male, british, australian) or full voice ID
            rate: Speech rate adjustment (e.g., "+0%", "+20%", "-10%")
            pitch: Pitch adjustment (e.g., "+0Hz", "+2Hz", "-2Hz")
        """
        self.voice = voice or self.DEFAULT_VOICE
        self.rate = rate
        self.pitch = pitch
        
        if not EDGE_TTS_AVAILABLE:
            print("⚠ edge-tts not available, TTS will use fallback")
            self._edge_available = False
        else:
            self._edge_available = True
    
    def speak(self, text, block=True):
        """
        Speak the given text.
        
        Args:
            text: Text to speak
            block: If True, wait for speech to complete. If False, return immediately.
        """
        if not text:
            return
        
        if self._edge_available:
            self._speak_edge(text, block)
        else:
            self._speak_fallback(text, block)
    
    def _speak_edge(self, text, block):
        """Speak using Edge TTS."""
        print(f"🗣️ Speaking: {text[:50]}{'...' if len(text) > 50 else ''}")
        
        async def speak():
            # Resolve voice
            voice_id = self.VOICES.get(self.voice, self.voice)
            
            # Create communicate object
            communicate = edge_tts.Communicate(text, voice_id, rate=self.rate, pitch=self.pitch)
            
            # Save to temp file
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
                temp_file = f.name
            
            await communicate.save(temp_file)
            return temp_file
        
        # Run async
        import asyncio
        
        try:
            temp_file = asyncio.run(speak())
            
            # Play audio
            self._play_audio(temp_file)
            
            # Wait if blocking
            if block:
                time.sleep(0.5)  # Small delay for playback to start
            
            # Cleanup
            if os.path.exists(temp_file):
                os.unlink(temp_file)
                
        except Exception as e:
            print(f"⚠ TTS error: {e}")
            self._speak_fallback(text, block)
    
    def _play_audio(self, audio_file):
        """Play audio file."""
        # Try different players
        players = ["ffplay", "paplay", "aplay", "play", "mpg123", "mpv"]
        
        for player in players:
            if subprocess.run(["which", player], capture_output=True).returncode == 0:
                try:
                    if player == "ffplay":
                        # ffplay with auto-exit
                        subprocess.Popen(
                            [player, "-nodisp", "-autoexit", "-loglevel", "quiet", audio_file],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                    elif player == "paplay" or player == "aplay":
                        # PulseAudio/ALSA players
                        subprocess.Popen(
                            [player, audio_file],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                    else:
                        subprocess.Popen(
                            [player, audio_file],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                    return
                except Exception:
                    continue
        
        print("⚠ No audio player found")
    
    def _speak_fallback(self, text, block):
        """Fallback TTS using gtts or say command."""
        print(f"🗣️ Speaking (fallback): {text[:50]}{'...' if len(text) > 50 else ''}")
        
        # Try gtts
        try:
            from gtts import gTTS
            
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
                temp_file = f.name
            
            tts = gTTS(text=text, lang="en")
            tts.save(temp_file)
            
            self._play_audio(temp_file)
            
            if os.path.exists(temp_file):
                os.unlink(temp_file)
                
        except ImportError:
            # Try macOS say command
            if sys.platform == "darwin":
                subprocess.Popen(["say", text])
            # Try espeak (Linux)
            elif subprocess.run(["which", "espeak"], capture_output=True).returncode == 0:
                subprocess.Popen(["espeak", text])
            else:
                print("⚠ No TTS backend available")
                print("   Install: pip install gtts")
                print("   Or: sudo apt install espeak")


def check_voice_setup():
    """
    Check if voice features are properly set up.
    
    Returns:
        dict with status of each component
    """
    status = {
        "whisper": WHISPER_AVAILABLE,
        "edge_tts": EDGE_TTS_AVAILABLE,
        "sounddevice": SOUNDDEVICE_AVAILABLE,
        "ffmpeg": subprocess.run(["which", "ffmpeg"], capture_output=True).returncode == 0,
        "arecord": subprocess.run(["which", "arecord"], capture_output=True).returncode == 0,
        "rec": subprocess.run(["which", "rec"], capture_output=True).returncode == 0,
    }
    
    return status


def print_voice_status():
    """Print voice setup status."""
    print("🎤 Voice Features Status:")
    print("-" * 30)
    
    status = check_voice_setup()
    
    checks = [
        ("Whisper (STT)", status["whisper"]),
        ("Edge TTS", status["edge_tts"]),
        ("Sounddevice", status["sounddevice"]),
        ("FFmpeg", status["ffmpeg"]),
        ("arecord (Linux)", status["arecord"]),
        ("rec (sox)", status["rec"]),
    ]
    
    for name, available in checks:
        icon = "✓" if available else "✗"
        print(f"   {icon} {name}")
    
    print()
    
    if not status["whisper"]:
        print("📦 Install Whisper: pip install openai-whisper")
    if not status["edge_tts"]:
        print("📦 Install TTS: pip install edge-tts")
    if not status["sounddevice"]:
        print("📦 Install audio capture: pip install sounddevice numpy scipy")
    
    print()


if __name__ == "__main__":
    print_voice_status()
