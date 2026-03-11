# Nanobot: Scribe
# Summarizes long text and chat threads

def summarize(text, max_length=100):
    """Summarize text to max_length words"""
    words = text.split()
    if len(words) <= max_length:
        return text
    return " ".join(words[:max_length]) + "..."

def process(input_text, context=None):
    """Main nanobot entry point"""
    return {
        "nanobot": "scribe",
        "action": "summarize",
        "result": summarize(input_text),
        "context": context
    }
