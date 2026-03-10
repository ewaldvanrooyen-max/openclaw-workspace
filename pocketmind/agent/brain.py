"""
PocketMind Brain Module

Handles model loading and inference using llama.cpp (via llama-cpp-python).
Designed for fully offline operation - no network calls required.
"""

import os
import sys
from typing import Optional, List, Dict, Tuple


class BrainError(Exception):
    """Base exception for Brain errors."""
    pass


class ModelNotFoundError(BrainError):
    """Raised when model file is not found."""
    pass


class ModelLoadError(BrainError):
    """Raised when model fails to load."""
    pass


class GenerationError(BrainError):
    """Raised when text generation fails."""
    pass


class Brain:
    """
    The brain handles loading the LLM model and generating responses.
    
    Designed for offline-first operation:
    - No network calls ever made
    - All inference happens locally
    - Model loaded from local filesystem only
    """
    
    # Default stop sequences for common models
    DEFAULT_STOP = ["</s>", "<|endoftext|>", "<|im_end|>"]
    
    def __init__(
        self, 
        model_path: str,
        n_ctx: int = 512,
        n_threads: int = 4,
        n_gpu_layers: int = 0,
        verbose: bool = False,
        offline_mode: bool = True
    ):
        """
        Initialize the brain with a model.
        
        Args:
            model_path: Path to the GGUF model file
            n_ctx: Context length (default: 512, max 2048 for small models)
            n_threads: Number of CPU threads (default: 4)
            n_gpu_layers: Number of layers to offload to GPU (0 = CPU only)
            verbose: Enable verbose logging
            offline_mode: If True, ensures no network operations (default: True)
        """
        self.model_path = model_path
        self.n_ctx = n_ctx
        self.n_threads = n_threads
        self.n_gpu_layers = n_gpu_layers
        self.verbose = verbose
        self.offline_mode = offline_mode
        
        self._llm = None
        self._loaded = False
        self._load_error: Optional[str] = None
        
        # Try to load the model
        self._load_model()
    
    def _load_model(self) -> None:
        """Load the LLM model with comprehensive error handling."""
        # Validate model path exists
        if not self.model_path:
            self._load_error = "No model path specified"
            raise ModelNotFoundError(self._load_error)
        
        if not os.path.exists(self.model_path):
            self._load_error = f"Model file not found: {self.model_path}"
            raise ModelNotFoundError(self._load_error)
        
        # Validate it's a file, not a directory
        if not os.path.isfile(self.model_path):
            self._load_error = f"Model path is not a file: {self.model_path}"
            raise ModelNotFoundError(self._load_error)
        
        # Check file size (warn if suspiciously small)
        file_size = os.path.getsize(self.model_path)
        if file_size < 1_000_000:  # Less than 1MB
            print(f"⚠ Warning: Model file is very small ({file_size} bytes)")
            print("  This may be an invalid or corrupted model file.")
        
        # Try to import llama_cpp
        try:
            from llama_cpp import Llama
        except ImportError as e:
            self._load_error = f"llama-cpp-python not installed: {e}"
            raise ModelLoadError(
                "llama-cpp-python not installed. "
                "Install with: pip install llama-cpp-python"
            )
        
        # Try to load the model
        try:
            # Build kwargs safely
            llm_kwargs = {
                "model_path": self.model_path,
                "n_ctx": self.n_ctx,
                "n_threads": self.n_threads,
                "verbose": self.verbose,
            }
            
            # Only add n_gpu_layers if explicitly set (not default 0)
            # This avoids issues on devices without GPU support
            if self.n_gpu_layers > 0:
                llm_kwargs["n_gpu_layers"] = self.n_gpu_layers
            
            self._llm = Llama(**llm_kwargs)
            self._loaded = True
            
        except Exception as e:
            self._load_error = str(e)
            raise ModelLoadError(f"Failed to load model: {e}")
    
    def generate(
        self, 
        prompt: str,
        max_tokens: int = 128,
        temperature: float = 0.7,
        top_p: float = 0.9,
        repeat_penalty: float = 1.1,
        stop: Optional[List[str]] = None
    ) -> str:
        """
        Generate a response from the model.
        
        All generation happens locally - no network calls.
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate (default: 128)
            temperature: Sampling temperature 0.0-2.0 (default: 0.7)
            top_p: Nucleus sampling threshold (default: 0.9)
            repeat_penalty: Penalty for repeated tokens (default: 1.1)
            stop: List of stop sequences
            
        Returns:
            Generated text response
        """
        # Validate model is loaded
        if not self._loaded or self._llm is None:
            return "⚠ Model not loaded. Cannot generate response."
        
        # Validate inputs
        if not prompt or not prompt.strip():
            return "⚠ Empty prompt provided."
        
        if max_tokens <= 0:
            return "⚠ max_tokens must be positive."
        
        if temperature < 0 or temperature > 2.0:
            return "⚠ temperature must be between 0.0 and 2.0."
        
        # Use default stop sequences if none provided
        if stop is None:
            stop = self.DEFAULT_STOP
        
        try:
            output = self._llm.create_completion(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                repeat_penalty=repeat_penalty,
                stop=stop
            )
            
            # Extract the generated text
            if not output or "choices" not in output:
                return "⚠ Invalid response from model."
            
            response = output["choices"][0]["text"]
            return response.strip()
            
        except Exception as e:
            return f"⚠ Generation error: {e}"
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        **kwargs
    ) -> str:
        """
        Generate a response in chat format.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            **kwargs: Additional generation parameters
            
        Returns:
            Assistant's response
        """
        if not self._loaded or self._llm is None:
            return "⚠ Model not loaded."
        
        if not messages:
            return "⚠ No messages provided."
        
        try:
            output = self._llm.create_chat_completion(
                messages=messages,
                **kwargs
            )
            
            if not output or "choices" not in output:
                return "⚠ Invalid response from model."
            
            response = output["choices"][0]["message"]["content"]
            return response.strip()
            
        except Exception as e:
            return f"⚠ Chat error: {e}"
    
    @property
    def is_loaded(self) -> bool:
        """Check if model is loaded and ready."""
        return self._loaded and self._llm is not None
    
    @property
    def is_offline(self) -> bool:
        """Confirm offline mode is active."""
        return self.offline_mode
    
    @property
    def model_name(self) -> str:
        """Get the model file name."""
        return os.path.basename(self.model_path)
    
    @property
    def load_error(self) -> Optional[str]:
        """Get the last load error if any."""
        return self._load_error
    
    def get_model_info(self) -> Dict:
        """Get information about the loaded model."""
        info = {
            "loaded": self._loaded,
            "model_path": self.model_path,
            "model_name": self.model_name,
            "n_ctx": self.n_ctx,
            "n_threads": self.n_threads,
            "n_gpu_layers": self.n_gpu_layers,
            "offline_mode": self.offline_mode,
            "error": self._load_error,
        }
        
        if self._llm:
            # Try to get model params if available
            try:
                info["model_params"] = self._llm.n_tokens()
            except Exception:
                pass
        
        return info
    
    def unload(self):
        """Unload the model to free memory."""
        if self._llm is not None:
            del self._llm
            self._llm = None
            self._loaded = False
            print("✓ Model unloaded")


class MockBrain:
    """
    A mock brain for testing without loading a model.
    Returns predefined responses for testing.
    
    This allows the CLI to function for development/testing
    without requiring the full model to be downloaded.
    """
    
    def __init__(self):
        self._loaded = True
        self._offline_mode = True
        self._model_name = "mock-model"
        
        # Storage - try to load profile
        try:
            from storage.json_store import ProfileStore, HistoryStore
            self.profile_store = ProfileStore()
            self.history_store = HistoryStore()
            self.user_profile = self.profile_store.load_profile()
        except Exception:
            self.profile_store = None
            self.history_store = None
            self.user_profile = None
    
    def has_profile(self) -> bool:
        """Check if user has completed onboarding."""
        return self.user_profile is not None and bool(self.user_profile.get("name"))
    
    def get_profile(self) -> Optional[Dict]:
        """Get the current user profile."""
        return self.user_profile
    
    def get_history(self, limit: int = 10) -> List[Dict]:
        """Get conversation history."""
        if self.history_store:
            return self.history_store.get_recent(limit)
        return []
    
    def clear_history(self) -> bool:
        """Clear conversation history."""
        if self.history_store:
            return self.history_store.clear_history()
        return False
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Return a mock response."""
        return "🤖 (Mock response) This is a test mode. Install a model to enable AI responses."
    
    def chat(self, messages, **kwargs) -> str:
        """Return a mock chat response."""
        return "🤖 (Mock) Hello! I'm running in test mode. Install a model to chat with the AI."
    
    @property
    def is_loaded(self) -> bool:
        return self._loaded
    
    @property
    def is_offline(self) -> bool:
        return self._offline_mode
    
    @property
    def model_name(self) -> str:
        return self._model_name
    
    def get_model_info(self) -> Dict:
        return {
            "loaded": True,
            "model_name": self._model_name,
            "offline_mode": self._offline_mode,
            "note": "Mock brain - no model loaded"
        }


def create_brain(
    model_path: str,
    n_ctx: int = 512,
    n_threads: int = 4,
    offline_mode: bool = True
) -> Tuple[Brain, bool]:
    """
    Factory function to create a Brain with error handling.
    
    Returns:
        Tuple of (brain_instance, success_bool)
    """
    try:
        brain = Brain(
            model_path=model_path,
            n_ctx=n_ctx,
            n_threads=n_threads,
            offline_mode=offline_mode
        )
        return brain, True
    except (ModelNotFoundError, ModelLoadError) as e:
        print(f"⚠ {e}")
        return None, False
    except Exception as e:
        print(f"⚠ Unexpected error: {e}")
        return None, False
