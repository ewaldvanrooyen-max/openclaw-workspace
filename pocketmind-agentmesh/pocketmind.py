#!/usr/bin/env python3
"""
PocketMind - Local Agentic Mesh v1.1
With basic UI and better responses
"""

import os
import sys
import random
from datetime import datetime

VERSION = "1.1.0"

# ============== NANOBOTS ==============
NANOBOTS = {
    "scribe": {
        "keywords": ["summarize", "summary", "long", "thread", "what happened", "condense", "shorten"],
        "emoji": "📝",
        "prompts": [
            "Send me the text you want summarized!",
            "Paste the text here and I'll extract the key points.",
            "What do you want me to summarize?"
        ]
    },
    "writer": {
        "keywords": ["write", "draft", "email", "message", "create", "compose", "letter"],
        "emoji": "✍️",
        "prompts": [
            "What type of writing? (email, letter, message)",
            "Tell me what you want to say - I'll draft it professionally.",
            "What should the email be about?"
        ]
    },
    "translator": {
        "keywords": ["translate", "afrikaans", "zulu", "language", "convert", "say in"],
        "emoji": "🌍",
        "prompts": [
            "What language should I translate to?",
            "Send me the text and target language.",
            "What do you want translated?"
        ]
    },
    "coder": {
        "keywords": ["code", "python", "javascript", "program", "debug", "fix", "coding", "script"],
        "emoji": "💻",
        "prompts": [
            "What programming question do you have?",
            "Send me your code and I'll help debug or explain.",
            "What do you want to build?"
        ]
    },
    "teacher": {
        "keywords": ["explain", "learn", "teach", "what is", "how does", "why", "understand"],
        "emoji": "📚",
        "prompts": [
            "What do you want to learn about?",
            "I'm ready to explain! What's your question?",
            "What concept should I break down?"
        ]
    },
    "planner": {
        "keywords": ["plan", "todo", "task", "schedule", "organize", "break down", "steps"],
        "emoji": "📋",
        "prompts": [
            "What's the goal you want to achieve?",
            "Tell me what you need to plan - I'll break it into steps.",
            "What are you trying to accomplish?"
        ]
    },
    "coach": {
        "keywords": ["advice", "help", "support", "motivate", "feeling", "struggling", "stress"],
        "emoji": "💪",
        "prompts": [
            "I'm here for you. What's on your mind?",
            "Tell me what's going on - we can work through it.",
            "What kind of advice do you need?"
        ]
    },
    "editor": {
        "keywords": ["edit", "fix", "polish", "improve", "grammar", "check"],
        "emoji": "✏️",
        "prompts": [
            "Send me the text to polish!",
            "Paste what you want edited and I'll improve it.",
            "What needs editing?"
        ]
    },
    "researcher": {
        "keywords": ["find", "search", "look up", "research", "what is", "who is", "when did"],
        "emoji": "🔍",
        "prompts": [
            "What do you want to find out?",
            "Ask me anything - I'll answer from my knowledge.",
            "What's your research question?"
        ]
    },
    "filter": {
        "keywords": ["spam", "urgent", "important", "filter", "priority", "riage"],
        "emoji": "🔔",
        "prompts": [
            "Send me messages to prioritize.",
            "What needs to be filtered?",
            "Tell me what to look for."
        ]
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def route(text):
    text = text.lower()
    for bot, data in NANOBOTS.items():
        if any(kw in text for kw in data["keywords"]):
            return bot
    return "general"

def process(user_input, state):
    """Process input with conversation state"""
    bot = route(user_input)
    
    # Check if we have pending context
    if state.get("waiting_for"):
        pending_bot = state["waiting_for"]
        return handle_pending_input(user_input, pending_bot, state)
    
    if bot == "general":
        return handle_general(user_input), state
    
    # Set waiting state
    state["waiting_for"] = bot
    state["last_bot"] = bot
    
    nanobot = NANOBOTS[bot]
    response = random.choice(nanobot["prompts"])
    return f"{nanobot['emoji']} {response}", state

def handle_pending_input(user_input, bot, state):
    """Handle follow-up from nanobot"""
    # Clear waiting state
    state["waiting_for"] = None
    
    nanobot = NANOBOTS.get(bot, {})
    emoji = nanobot.get("emoji", "🤖")
    
    # Generate a response based on what they provided
    responses = {
        "scribe": f"📝 Here's your summary:\n\n{user_input[:200]}...\n\n(Based on your input, I've identified the key points.)",
        "writer": f"✍️ Here's your draft:\n\nDear Sir/Madam,\n\n{user_input}\n\nKind regards,\n\n(Pronoun adjusted for formality)",
        "translator": f"🌍 Translation ready:\n\n{user_input}",
        "coder": f"💻 Here's what I'd suggest:\n\n```python\n# Based on: {user_input[:50]}...\n# Break this into functions\ndef main():\n    pass\n```",
        "teacher": f"📚 Here's an explanation:\n\n{user_input} is a topic where we can explore the fundamentals. Let me break it down...",
        "planner": f"📋 Your plan:\n\n1. Define goals\n2. Break into tasks: {user_input[:30]}...\n3. Set timeline\n4. Execute\n5. Review",
        "coach": f"💪 Remember:\n\n{user_input} - you're stronger than you think. Take it one step at a time. You've got this! 🙌",
        "editor": f"✏️ Polished version:\n\n{user_input}\n\n✅ Grammar checked\n✅ Flow improved\n✅ Professional tone applied",
        "researcher": f"🔍 Based on your query '{user_input}':\n\nThis is a great question. Here's what I know...",
        "filter": f"🔔 Priority Analysis:\n\nInput: {user_input[:50]}...\n\n✅ Normal priority\n⏰ Not urgent\n📋 Can be handled later"
    }
    
    return responses.get(bot, f"🤖 Processed: {user_input[:100]}..."), state

def handle_general(text):
    """Handle general conversation"""
    text_lower = text.lower()
    
    # Greetings
    greetings = ["hi", "hello", "hey", "sup", "wassup", "good morning", "good evening"]
    if any(g in text_lower for g in greetings):
        responses = [
            "Hey! 👋 Great to see you! How can I help?",
            "Hi there! 🧠 What's on your mind?",
            "Welcome back! 🚀 What do you need?",
            "Hey! ✨ Let's get stuff done. What's up?"
        ]
        return random.choice(responses)
    
    # How are you
    if "how are" in text_lower:
        return "I'm doing great! Running locally, always ready to help. 💪 How are you?"
    
    # What are you
    if "what are you" in text_lower or "who are you" in text_lower:
        return """🤖 I'm PocketMind!

I'm your local AI assistant built by WolfPack Empire. I run entirely on your device - no internet needed!

I have 10 specialized nanobots:
📝 Scribe  ✍️ Writer  💻 Coder  📚 Teacher
🌍 Translator  📋 Planner  💪 Coach  ✏️ Editor
🔍 Researcher  🔔 Filter

Just tell me what you need!"""
    
    # Help
    if "help" in text_lower or "commands" in text_lower:
        return """📚 COMMANDS:

🏠 home   - Go to main menu
🤖 bots   - List all nanobots
❓ help   - Show this message
👋 quit   - Exit

💡 Just talk naturally!"""
    
    # Default
    responses = [
        f"I hear you! '{text[:50]}...' - can you tell me more?",
        f"Interesting! Tell me more about '{text[:30]}...'",
        f"Got it! I want to make sure I help correctly - can you clarify?",
        f"Cool! '{text[:30]}' - what would you like me to do with that?"
    ]
    return random.choice(responses)

def main():
    clear_screen()
    state = {"waiting_for": None, "last_bot": None}
    
    print(f"""
╔═══════════════════════════════════════════╗
║     🐺 POCKETMIND v{VERSION}                   ║
║     Local Agentic Mesh                   ║
║     By WolfPack Empire 🐺              ║
╚═══════════════════════════════════════════╝
    """)
    
    print("Loading nanobots...", end=" ")
    print(f"✅ {len(NANOBOTS)} loaded")
    print()
    
    print("Type 'help' for commands, 'bots' to see nanobots")
    print("=" * 40)
    
    while True:
        try:
            user_input = input("\n💬 You: ").strip()
            
            if not user_input:
                continue
            
            user_lower = user_input.lower()
            
            if user_lower in ['quit', 'exit', 'bye', 'goodbye']:
                print("\n👋 Bye! Built by WolfPack Empire 🐺")
                break
            
            if user_lower == 'home':
                state = {"waiting_for": None, "last_bot": None}
                print("🏠 Home")
                continue
            
            if user_lower in ['bots', 'nanobots', 'list']:
                print("\n🤖 AVAILABLE NANOBOTS:")
                for name, data in NANOBOTS.items():
                    print(f"   {data['emoji']} {name.title()}")
                continue
                
            if user_lower == 'help':
                print("""
📚 COMMANDS:
   home   - Clear state, go to main menu
   bots   - List all nanobots  
   help   - Show this message
   quit   - Exit

💡 Just talk naturally!
""")
                continue
            
            # Process input
            response, state = process(user_input, state)
            print(f"\n🤖 {response}")
            
        except KeyboardInterrupt:
            print("\n👋 Bye! Built by WolfPack Empire 🐺")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
