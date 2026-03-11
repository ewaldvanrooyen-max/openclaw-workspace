# Nanobot: Router
# Intent classification and routing

def route(input_text):
    """Route to the right nanobot"""
    input_lower = input_text.lower()
    
    routes = {
        "scribe": ["summarize", "summary", "long", "thread", "what happened"],
        "writer": ["write", "draft", "email", "message", "create"],
        "translator": ["translate", "afrikaans", "zulu", "language", "convert"],
        "coder": ["code", "python", "javascript", "program", "debug"],
        "teacher": ["explain", "learn", "teach", "what is", "how does"],
        "planner": ["plan", "todo", "task", "schedule", "organize"],
        "coach": ["advice", "help", "support", "motivate", "feeling"],
        "editor": ["edit", "fix", "polish", "improve", "grammar"],
        "researcher": ["find", "search", "look up", "research"],
    }
    
    for bot, keywords in routes.items():
        if any(kw in input_lower for kw in keywords):
            return bot
    return "general"

def process(input_text, context=None):
    bot = route(input_text)
    return {
        "nanobot": "router",
        "action": "route",
        "target": bot,
        "input": input_text,
        "context": context
    }
