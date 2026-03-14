#!/usr/bin/env python3
"""
TTS Script using Kokoro-82M
Generates audio from text for Telegram voice notes
"""
import os
import sys
import argparse
from kokoro import KPipeline
import soundfile as sf

# Available voices: af_heart, af_sarah, am_michael, am_fen, bf_emma, bm_george
# 'a' = American English, 'b' = British English

def generate_speech(text, voice='af_heart', speed=1, output_file='output.wav', lang='a'):
    """Generate speech from text using Kokoro TTS"""
    print(f"Generating speech with voice: {voice}")
    print(f"Text: {text[:50]}...")
    
    pipeline = KPipeline(lang_code=lang)
    generator = pipeline(text, voice=voice, speed=speed)
    
    # Collect all audio chunks
    audio_chunks = []
    for i, (gs, ps, audio) in enumerate(generator):
        audio_chunks.append(audio)
        print(f"Chunk {i}: {len(audio)} samples")
    
    if audio_chunks:
        # Concatenate all chunks
        import numpy as np
        full_audio = np.concatenate(audio_chunks)
        
        # Save to file
        sf.write(output_file, full_audio, 24000)
        print(f"Saved to: {output_file}")
        return output_file
    else:
        print("No audio generated!")
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kokoro TTS')
    parser.add_argument('--text', '-t', required=True, help='Text to speak')
    parser.add_argument('--voice', '-v', default='af_heart', help='Voice to use')
    parser.add_argument('--output', '-o', default='/tmp/tts_output.wav', help='Output file')
    parser.add_argument('--speed', '-s', type=float, default=1.0, help='Speed (0.5-2.0)')
    parser.add_argument('--lang', '-l', default='a', help='Language code (a=en-US, b=en-GB)')
    
    args = parser.parse_args()
    generate_speech(args.text, args.voice, args.speed, args.output, args.lang)
