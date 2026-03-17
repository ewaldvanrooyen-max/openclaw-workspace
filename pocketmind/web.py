#!/usr/bin/env python3
"""
PocketPal Web Interface

Simple Flask web interface for testing PocketPal from mobile.
"""

import os
import sys
import json
import requests
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, jsonify, redirect, url_for
from storage.json_store import ProfileStore, HistoryStore

app = Flask(__name__, template_folder='templates')

# MiniMax Configuration
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY", "")
MINIMAX_BASE_URL = os.environ.get("MINIMAX_BASE_URL", "https://api.minimax.io/v1")
MINIMAX_MODEL = os.environ.get("MINIMAX_MODEL", "MiniMax-M2.5")
USE_MINIMAX = bool(MINIMAX_API_KEY)

# Create templates folder
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
os.makedirs(TEMPLATE_DIR, exist_ok=True)

# Initialize stores
DATA_DIR = os.path.expanduser("~/.pocketmind")
profile_store = ProfileStore(DATA_DIR)
history_store = HistoryStore(DATA_DIR)


class MiniMaxBrain:
    """MiniMax API brain for cloud inference."""
    
    def __init__(self):
        self._loaded = True
        self._offline_mode = False
        self._model_name = MINIMAX_MODEL
        self._api_key = MINIMAX_API_KEY
        self._base_url = MINIMAX_BASE_URL
        
    def chat(self, messages, **kwargs) -> str:
        """Generate response using MiniMax API."""
        if not self._api_key:
            return "⚠ MiniMax API key not configured. Please set MINIMAX_API_KEY environment variable."
        
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._api_key}"
            }
            
            # Convert messages to MiniMax format
            mm_messages = []
            for msg in messages:
                role = msg.get("role", "user")
                if role == "assistant":
                    role = "assistant"
                elif role == "system":
                    role = "system"
                else:
                    role = "user"
                mm_messages.append({"role": role, "content": msg.get("content", "")})
            
            payload = {
                "model": self._model_name,
                "messages": mm_messages,
                "temperature": kwargs.get("temperature", 0.7),
                "max_tokens": kwargs.get("max_tokens", 1024)
            }
            
            response = requests.post(
                f"{self._base_url}/text/chatcompletion_v2",
                headers=headers,
                json=payload,
                timeout=60
            )
            
            if response.status_code != 200:
                return f"⚠ API Error: {response.status_code} - {response.text}"
            
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "No response")
            
        except Exception as e:
            return f"⚠ Error: {str(e)}"
    
    @property
    def is_loaded(self) -> bool:
        return self._loaded
    
    @property
    def is_offline(self) -> bool:
        return self._offline_mode
    
    @property
    def model_name(self) -> str:
        return self._model_name


# Initialize brain based on configuration
if USE_MINIMAX:
    from agent.brain import MockBrain
    brain = MiniMaxBrain()
    print(f"🧠 Using MiniMax API: {MINIMAX_MODEL}")
else:
    from agent.brain import MockBrain
    brain = MockBrain()
    print("🧠 Using MockBrain (set MINIMAX_API_KEY to enable MiniMax)")

# Health endpoint
@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "model": brain.model_name,
        "provider": "minimax" if USE_MINIMAX else "mock",
        "offline": brain.is_offline,
        "timestamp": str(Path("/").stat().st_ctime) if False else ""
    })


# Create base template
BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="theme-color" content="#161b22">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="manifest" href="static/manifest.json">
    <link rel="icon" type="image/png" href="static/icon-192.png">
    <link rel="apple-touch-icon" href="static/icon-192.png">
    <title>{% block title %}PocketPal{% endblock %}</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0d1117;
            color: #e6edf3;
            min-height: 100vh;
            padding-bottom: 80px;
        }
        .header {
            background: #161b22;
            padding: 16px;
            border-bottom: 1px solid #30363d;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .header h1 {
            font-size: 20px;
            color: #58a6ff;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 16px;
        }
        .card {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
        }
        .btn {
            display: inline-block;
            background: #238636;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
            width: 100%;
            text-align: center;
        }
        .btn-secondary {
            background: #30363d;
        }
        .btn:hover { opacity: 0.9; }
        input, select, textarea {
            width: 100%;
            padding: 12px;
            background: #0d1117;
            border: 1px solid #30363d;
            border-radius: 6px;
            color: #e6edf3;
            font-size: 16px;
            margin-bottom: 12px;
        }
        input:focus, textarea:focus {
            outline: none;
            border-color: #58a6ff;
        }
        .nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #161b22;
            border-top: 1px solid #30363d;
            display: flex;
            justify-content: space-around;
            padding: 12px;
        }
        .nav a {
            color: #8b949e;
            text-decoration: none;
            font-size: 12px;
            text-align: center;
        }
        .nav a.active {
            color: #58a6ff;
        }
        .nav-icon {
            font-size: 24px;
            display: block;
            margin-bottom: 4px;
        }
        .message {
            padding: 12px 16px;
            margin-bottom: 12px;
            border-radius: 12px;
            max-width: 85%;
        }
        .message.user {
            background: #238636;
            margin-left: auto;
            border-bottom-right-radius: 4px;
        }
        .message.assistant {
            background: #21262d;
            border-bottom-left-radius: 4px;
        }
        .chat-messages {
            max-height: calc(100vh - 200px);
            overflow-y: auto;
            padding-bottom: 20px;
        }
        .chat-input {
            position: fixed;
            bottom: 60px;
            left: 0;
            right: 0;
            background: #161b22;
            padding: 12px;
            border-top: 1px solid #30363d;
            display: flex;
            gap: 8px;
        }
        .chat-input input {
            flex: 1;
            margin: 0;
        }
        .chat-input button {
            background: #238636;
            border: none;
            color: white;
            padding: 12px 20px;
            border-radius: 6px;
            cursor: pointer;
        }
        .profile-field {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #30363d;
        }
        .profile-field:last-child { border-bottom: none; }
        .profile-label { color: #8b949e; }
        .profile-value { color: #e6edf3; }
        .status-badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            background: #238636;
        }
        .empty-state {
            text-align: center;
            padding: 40px 20px;
            color: #8b949e;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 PocketPal</h1>
    </div>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <nav class="nav">
        <a href="/" class="{{ 'active' if page == 'home' else '' }}">
            <span class="nav-icon">🏠</span>
            Home
        </a>
        <a href="/onboarding" class="{{ 'active' if page == 'onboarding' else '' }}">
            <span class="nav-icon">👤</span>
            Profile
        </a>
        <a href="/chat" class="{{ 'active' if page == 'chat' else '' }}">
            <span class="nav-icon">💬</span>
            Chat
        </a>
    </nav>
    {% block scripts %}{% endblock %}
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('static/sw.js')
                    .then(reg => console.log('SW registered'))
                    .catch(err => console.log('SW registration failed'));
            });
        }
    </script>
</body>
</html>
"""

# Write base template
with open(os.path.join(TEMPLATE_DIR, 'base.html'), 'w') as f:
    f.write(BASE_TEMPLATE)


# Write home template
HOME_TEMPLATE = """{% extends "base.html" %}
{% block title %}PocketPal - Home{% endblock %}
{% block content %}
    {% if has_profile %}
        <div class="card">
            <h2>Welcome back, {{ profile.name }}! 👋</h2>
            <p style="color: #8b949e; margin-top: 8px;">
                {{ profile.response_style }} • {{ profile.goal_display }}
            </p>
        </div>
        
        <div class="card">
            <h3>Quick Stats</h3>
            <div class="profile-field">
                <span class="profile-label">Schedule</span>
                <span class="profile-value">{{ profile.schedule_display }}</span>
            </div>
            <div class="profile-field">
                <span class="profile-label">Timezone</span>
                <span class="profile-value">{{ profile.timezone }}</span>
            </div>
            <div class="profile-field">
                <span class="profile-label">Tone</span>
                <span class="profile-value">{{ profile.tone }}</span>
            </div>
        </div>
        
        <a href="/chat" class="btn">Start Chatting</a>
    {% else %}
        <div class="card">
            <h2>Welcome to PocketPal! 🎉</h2>
            <p style="color: #8b949e; margin-top: 8px;">
                Your personal AI assistant. Let's get you set up!
            </p>
        </div>
        
        <a href="/onboarding" class="btn">Start Onboarding</a>
    {% endif %}
{% endblock %}
"""

with open(os.path.join(TEMPLATE_DIR, 'home.html'), 'w') as f:
    f.write(HOME_TEMPLATE)


# Write onboarding template
ONBOARDING_TEMPLATE = """{% extends "base.html" %}
{% block title %}PocketPal - Profile{% endblock %}
{% block content %}
    <div class="card">
        <h2>👤 Your Profile</h2>
        {% if has_profile %}
            <p style="color: #8b949e; margin-bottom: 16px;">Your current profile settings</p>
            
            <div class="profile-field">
                <span class="profile-label">Name</span>
                <span class="profile-value">{{ profile.name }}</span>
            </div>
            <div class="profile-field">
                <span class="profile-label">Goal</span>
                <span class="profile-value">{{ profile.goal_display }}</span>
            </div>
            <div class="profile-field">
                <span class="profile-label">Schedule</span>
                <span class="profile-value">{{ profile.schedule_display }}</span>
            </div>
            <div class="profile-field">
                <span class="profile-label">Timezone</span>
                <span class="profile-value">{{ profile.timezone }}</span>
            </div>
            <div class="profile-field">
                <span class="profile-label">Style</span>
                <span class="profile-value">{{ profile.response_style }}</span>
            </div>
            
            <a href="/onboarding/reset" class="btn btn-secondary" style="margin-top: 16px;">Reset Profile</a>
        {% else %}
            <p style="color: #8b949e;">No profile yet. Complete onboarding to get started!</p>
        {% endif %}
    </div>
    
    <div class="card">
        <h3>✏️ Edit Profile</h3>
        <p style="color: #8b949e; margin-bottom: 16px;">Update your settings</p>
        
        <form method="post" action="/onboarding/update">
            <label>What should I call you?</label>
            <input type="text" name="name" value="{{ profile.name or '' }}" placeholder="Your name" required>
            
            <label>What's your main goal?</label>
            <select name="goal">
                <option value="productivity" {{ 'selected' if profile.goal == 'productivity' else '' }}>Productivity & Tasks</option>
                <option value="learning" {{ 'selected' if profile.goal == 'learning' else '' }}>Learning & Study</option>
                <option value="health" {{ 'selected' if profile.goal == 'health' else '' }}>Health & Fitness</option>
                <option value="creative" {{ 'selected' if profile.goal == 'creative' else '' }}>Creative Projects</option>
                <option value="general" {{ 'selected' if profile.goal == 'general' else '' }}>General Assistant</option>
            </select>
            
            <label>What's your typical schedule?</label>
            <select name="schedule_type">
                <option value="9-5_office_worker" {{ 'selected' if profile.schedule_type == '9-5_office_worker' else '' }}>9-5 Office Worker</option>
                <option value="flexible" {{ 'selected' if profile.schedule_type == 'flexible' else '' }}>Flexible Hours</option>
                <option value="night_owl" {{ 'selected' if profile.schedule_type == 'night_owl' else '' }}>Night Owl</option>
                <option value="early_bird" {{ 'selected' if profile.schedule_type == 'early_bird' else '' }}>Early Bird</option>
            </select>
            
            <label>How should I respond?</label>
            <select name="response_style">
                <option value="Brief & to the point" {{ 'selected' if profile.response_style == 'Brief & to the point' else '' }}>Brief & to the point</option>
                <option value="Detailed explanations" {{ 'selected' if profile.response_style == 'Detailed explanations' else '' }}>Detailed explanations</option>
                <option value="Casual conversation" {{ 'selected' if profile.response_style == 'Casual conversation' else '' }}>Casual conversation</option>
            </select>
            
            <button type="submit" class="btn">Save Profile</button>
        </form>
    </div>
{% endblock %}
"""

with open(os.path.join(TEMPLATE_DIR, 'onboarding.html'), 'w') as f:
    f.write(ONBOARDING_TEMPLATE)


# Write chat template
CHAT_TEMPLATE = """{% extends "base.html" %}
{% block title %}PocketPal - Chat{% endblock %}
{% block content %}
    <div class="chat-messages" id="messages">
        {% if not has_profile %}
            <div class="empty-state">
                <p>Complete onboarding first to start chatting!</p>
                <a href="/onboarding" class="btn" style="margin-top: 16px; width: auto;">Go to Profile</a>
            </div>
        {% elif messages|length == 0 %}
            <div class="empty-state">
                <p>👋 Hey there! How can I help you today?</p>
            </div>
        {% else %}
            {% for msg in messages %}
                <div class="message {{ msg.role }}">
                    {{ msg.content }}
                </div>
            {% endfor %}
        {% endif %}
    </div>
{% endblock %}

{% block scripts %}
<div class="chat-input">
    <input type="text" id="user-input" placeholder="Type a message..." {% if not has_profile %}disabled{% endif %}>
    <button onclick="sendMessage()" {% if not has_profile %}disabled{% endif %}>Send</button>
</div>

<script>
    function scrollToBottom() {
        const msgs = document.getElementById('messages');
        msgs.scrollTop = msgs.scrollHeight;
    }
    scrollToBottom();
    
    async function sendMessage() {
        const input = document.getElementById('user-input');
        const message = input.value.trim();
        if (!message) return;
        
        // Add user message
        const messagesDiv = document.getElementById('messages');
        
        // Remove empty state if present
        const emptyState = messagesDiv.querySelector('.empty-state');
        if (emptyState) emptyState.remove();
        
        const userMsg = document.createElement('div');
        userMsg.className = 'message user';
        userMsg.textContent = message;
        messagesDiv.appendChild(userMsg);
        input.value = '';
        scrollToBottom();
        
        // Send to server
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message})
        });
        
        const data = await response.json();
        
        // Add assistant response
        const assistantMsg = document.createElement('div');
        assistantMsg.className = 'message assistant';
        assistantMsg.textContent = data.response;
        messagesDiv.appendChild(assistantMsg);
        scrollToBottom();
    }
    
    document.getElementById('user-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') sendMessage();
    });
</script>
{% endblock %}
"""

with open(os.path.join(TEMPLATE_DIR, 'chat.html'), 'w') as f:
    f.write(CHAT_TEMPLATE)


# Routes
@app.route('/')
def home():
    """Home page showing profile status."""
    profile = profile_store.load_profile()
    has_profile = profile is not None and bool(profile.get('name'))
    
    return render_template('home.html',
        page='home',
        profile=profile or {},
        has_profile=has_profile
    )


@app.route('/onboarding', methods=['GET'])
def onboarding():
    """Onboarding/profile management page."""
    profile = profile_store.load_profile()
    has_profile = profile is not None and bool(profile.get('name'))
    
    return render_template('onboarding.html',
        page='onboarding',
        profile=profile or {},
        has_profile=has_profile
    )


@app.route('/onboarding/update', methods=['POST'])
def update_profile():
    """Update user profile."""
    name = request.form.get('name', '').strip()
    goal = request.form.get('goal', 'general')
    schedule_type = request.form.get('schedule_type', '9-5_office_worker')
    response_style = request.form.get('response_style', 'Brief & to the point')
    
    goal_map = {
        'productivity': 'Productivity & tasks',
        'learning': 'Learning & study',
        'health': 'Health & fitness',
        'creative': 'Creative projects',
        'general': 'General assistance'
    }
    
    schedule_map = {
        '9-5_office_worker': '9-5 office worker',
        'flexible': 'Flexible hours',
        'night_owl': 'Night owl',
        'early_bird': 'Early bird'
    }
    
    profile = {
        'name': name,
        'goal': goal,
        'goal_display': goal_map.get(goal, goal),
        'schedule_type': schedule_type,
        'schedule_display': schedule_map.get(schedule_type, schedule_type),
        'timezone': 'UTC',
        'response_style': response_style,
        'detail_level': 'brief',
        'tone': 'direct',
        'important_dates': [],
        'personal_context': {'notes': ''},
        'preferences': {'use_emojis': True, 'include_greetings': True},
    }
    
    profile_store.save_profile(profile)
    return redirect(url_for('home'))


@app.route('/onboarding/reset')
def reset_profile():
    """Reset/clear user profile."""
    profile_store.clear_profile()
    return redirect(url_for('onboarding'))


@app.route('/chat')
def chat():
    """Chat interface page."""
    profile = profile_store.load_profile()
    has_profile = profile is not None and bool(profile.get('name'))
    
    # Get recent messages
    messages = history_store.get_recent(20) if has_profile else []
    
    return render_template('chat.html',
        page='chat',
        profile=profile or {},
        has_profile=has_profile,
        messages=messages
    )


@app.route('/api/chat', methods=['POST'])
def api_chat():
    """Chat API endpoint."""
    data = request.get_json()
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'response': 'Please enter a message.'})
    
    # Get profile for context
    profile = profile_store.load_profile()
    if not profile or not profile.get('name'):
        return jsonify({'response': 'Please complete onboarding first!'})
    
    # Get conversation history
    history = history_store.get_recent(10)
    
    # Build messages for brain
    messages = [{"role": "user" if m.get("role") == "user" else "assistant", 
                 "content": m.get("content", "")} for m in history]
    messages.append({"role": "user", "content": user_message})
    
    # Generate response
    try:
        response = brain.chat(messages)
    except Exception as e:
        response = f"Sorry, I encountered an error: {str(e)}"
    
    # Save to history
    history_store.add_message("user", user_message)
    history_store.add_message("assistant", response)
    
    return jsonify({'response': response})


if __name__ == '__main__':
    print("=" * 50)
    print("🤖 PocketPal Web Interface")
    print("=" * 50)
    print("Open http://76.13.195.238:5005 on your phone!")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5005, debug=True)

@app.route('/download')
def download():
    return render_template('download.html', page='download')
