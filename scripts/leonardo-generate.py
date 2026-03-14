#!/usr/bin/env python3
"""
Leonardo.ai Image Generator for ContentEngen
Generates images and saves to library
"""
import os
import sys
import json
import argparse
import requests
from datetime import datetime

# Config
API_URL = "https://api.leonardo.ai/v1/generations"
LIBRARY_DIR = "/root/.openclaw/workspace/contentengen-library/images"

# Load API key
CREDENTIALS_FILE = os.path.expanduser("~/.openclaw/credentials/leonardo-api.json")

def load_api_key():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE) as f:
            data = json.load(f)
            return data.get("api_key")
    return os.environ.get("LEONARDO_API_KEY")

def generate_image(prompt, model="lucideon", width=1024, height=1024):
    """Generate an image using Leonardo.ai API"""
    api_key = load_api_key()
    if not api_key:
        print("Error: No Leonardo API key found")
        return None
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": prompt,
        "modelId": model,
        "width": width,
        "height": height,
        "guidance_scale": 7,
        "num_images": 1
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        generation_id = data.get("generationId")
        print(f"Generation started: {generation_id}")
        return generation_id
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def generate_from_manifest(manifest_file, count=10, volume=None):
    """Generate images from manifest"""
    # Simple manifest-based generation
    prompts = [
        ("Sovereign", "Corporate boardroom meeting with modern furniture"),
        ("Sovereign", "Executive office with glass walls and city view"),
        ("Solarpunk", "Futuristic eco-city with solar panels and green buildings"),
        ("Solarpunk", "Sustainable farm with vertical gardens"),
        ("Sanctuary", "Peaceful meditation room with natural light"),
        ("Sanctuary", "Wellness spa with calming colors"),
        ("Glitch", "Neon city street at night with rain"),
        ("Glitch", "Cyberpunk alley with holographic signs"),
        ("Sovereign", "Professional business meeting in progress"),
        ("Solarpunk", "Clean energy wind farm at sunset"),
    ]
    
    results = []
    for i, (vol, prompt) in enumerate(prompts[:count]):
        if volume and vol != volume:
            continue
        print(f"Generating [{i+1}/{count}]: {vol} - {prompt[:30]}...")
        result = generate_image(prompt)
        results.append({"volume": vol, "prompt": prompt, "generation_id": result})
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Leonardo.ai Image Generator")
    parser.add_argument("--prompt", "-p", help="Prompt for image generation")
    parser.add_argument("--count", "-c", type=int, default=1, help="Number of images to generate")
    parser.add_argument("--volume", "-v", help="Filter by volume (Sovereign, Solarpunk, Sanctuary, Glitch)")
    parser.add_argument("--model", "-m", default="lucideon", help="Model to use")
    
    args = parser.parse_args()
    
    if args.prompt:
        # Single generation
        gen_id = generate_image(args.prompt, args.model)
        print(f"Generation ID: {gen_id}")
    else:
        # Batch from manifest
        results = generate_from_manifest(None, args.count, args.volume)
        print(f"Generated {len(results)} images")

if __name__ == "__main__":
    main()
