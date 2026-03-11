#!/usr/bin/env python3
"""
PocketMind Core - Local Agentic Mesh
Based on llama.cpp for mobile inference
"""

import os
import sys
import json
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
MODELS_DIR = BASE_DIR / "models"
CONFIG_DIR = BASE_DIR / "configs"
NANOBOTS_DIR = BASE_DIR / "src" / "nanobots"

# Config
DEFAULT_MODEL = "smollm2-360m-q4_k_m.gguf"
CONTEXT_SIZE = 2048
THREADS = 4

class PocketMind:
    def __init__(self, model_path=None):
        self.model_path = model_path or (MODELS_DIR / DEFAULT_MODEL)
        self.model = None
        self.loaded = False
        
    def load(self):
        """Load the model"""
        if not self.model_path.exists():
            print(f"❌ Model not found: {self.model_path}")
            print(f"📥 Download: https://huggingface.co/TheBloke/SmolLM2-360M-Instruct-GGUF")
            return False
            
        print(f"🧠 Loading {self.model_path.name}...")
        # TODO: Integrate llama.cpp
        # For now, use mock mode
        self.loaded = True
        print("✅ Model loaded (mock mode)")
        return True
    
    def generate(self, prompt, max_tokens=256):
        """Generate response"""
        if not self.loaded:
            return "Model not loaded. Run load() first."
        
        # TODO: Real inference
        return f"🤖 [PocketMind] Received: {prompt[:50]}..."
    
    def route(self, user_input):
        """Route to the right nanobot"""
        # Simple keyword-based routing
        input_lower = user_input.lower()
        
        routes = {
            "scribe": ["summarize", "summary", "summarise", "long"],
            "writer": ["write", "draft", "email", "message"],
            "translator": ["translate", "afrikaans", "zulu", "language"],
            "coder": ["code", "python", "javascript", "program"],
            "teacher": ["explain", "learn", "teach", "what is"],
            "planner": ["plan", "todo", "task", "schedule"],
            "coach": ["advice", "help", "motivate", "support"],
            "editor": ["edit", "fix", "polish", "improve"],
            "researcher": ["find", "search", "research", "look up"],
        }
        
        for bot, keywords in routes.items():
            if any(kw in input_lower for kw in keywords):
                return bot
        return "general"
    
    def run(self):
        """Main interaction loop"""
        print("""
🐺 PocketMind - Local Agentic Mesh
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type 'quit' to exit
Type 'load' to reload model
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """)
        
        if not self.load():
            print("⚠️ Running in mock mode")
            self.loaded = True
            
        while True:
            try:
                user_input = input("\n💬 You: ").strip()
                if not user_input:
                    continue
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye!")
                    break
                if user_input.lower() == 'load':
                    self.load()
                    continue
                    
                # Route to nanobot
                bot = self.route(user_input)
                print(f"📍 Routed to: {bot}")
                
                # Generate response
                response = self.generate(user_input)
                print(f"🤖 {response}")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break

if __name__ == "__main__":
    pm = PocketMind()
    pm.run()
