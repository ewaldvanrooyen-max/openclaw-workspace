# Nanobot: Writer
# Drafts emails, messages, content

def write(prompt, style="professional"):
    """Generate written content"""
    templates = {
        "professional": f"Dear Sir/Madam,\n\n{prompt}\n\nKind regards,",
        "casual": f"Hey,\n\n{prompt}\n\nBest,",
        "formal": f"To Whom It May Concern,\n\n{prompt}\n\nSincerely,"
    }
    return templates.get(style, templates["professional"])

def process(input_text, style="professional", context=None):
    return {
        "nanobot": "writer", 
        "action": "write",
        "result": write(input_text, style),
        "style": style,
        "context": context
    }
