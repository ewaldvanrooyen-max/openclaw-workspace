#!/usr/bin/env python3
"""
Kaiber.ai Video Generator for ContentEngen
Generates videos and saves to library
"""
import os
import sys
import json
import argparse
import requests
from datetime import datetime

# Config
API_URL = "https://api.kaiber.ai/v2/video/generate"
LIBRARY_DIR = "/root/.openclaw/workspace/contentengen-library/videos"

# Load API key
CREDENTIALS_FILE = os.path.expanduser("~/.openclaw/credentials/kaiber-api.json")

def load_api_key():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE) as f:
            data = json.load(f)
            return data.get("api_key")
    return os.environ.get("KAIBER_API_KEY")

def generate_video(prompt, seconds=5, style="motion"):
    """Generate a video using Kaiber.ai API"""
    api_key = load_api_key()
    if not api_key:
        print("Error: No Kaiber API key found")
        return None
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": prompt,
        "duration": seconds,
        "style": style
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        video_id = data.get("id")
        print(f"Video generation started: {video_id}")
        return video_id
    except Exception as e:
        print(f"Error generating video: {e}")
        return None

def generate_from_manifest(count=3, volume=None):
    """Generate videos from manifest"""
    prompts = [
        ("Sovereign", "Corporate meeting with professional lighting"),
        ("Sovereign", "Business presentation on modern screens"),
        ("Solarpunk", "Futuristic city with flowing energy"),
        ("Solarpunk", "Eco-friendly technology in nature"),
        ("Sanctuary", "Calm water ripples in slow motion"),
        ("Sanctuary", "Peaceful forest with gentle movement"),
        ("Glitch", "Digital glitch effects on urban scene"),
        ("Glitch", "Neon lights reflecting in rain puddles"),
    ]
    
    results = []
    for i, (vol, prompt) in enumerate(prompts[:count*2]):
        if volume and vol != volume:
            continue
        if i >= count:
            break
        print(f"Generating [{i+1}/{count}]: {vol} - {prompt[:30]}...")
        result = generate_video(prompt)
        results.append({"volume": vol, "prompt": prompt, "video_id": result})
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Kaiber.ai Video Generator")
    parser.add_argument("--prompt", "-p", help="Prompt for video generation")
    parser.add_argument("--seconds", "-s", type=int, default=5, help="Video duration in seconds")
    parser.add_argument("--style", "-t", default="motion", help="Video style (motion, animation, anime, realistic)")
    parser.add_argument("--count", "-c", type=int, default=1, help="Number of videos to generate")
    parser.add_argument("--volume", "-v", help="Filter by volume")
    
    args = parser.parse_args()
    
    if args.prompt:
        # Single generation
        video_id = generate_video(args.prompt, args.seconds, args.style)
        print(f"Video ID: {video_id}")
    else:
        # Batch from manifest
        results = generate_from_manifest(args.count, args.volume)
        print(f"Generated {len(results)} videos")

if __name__ == "__main__":
    main()
