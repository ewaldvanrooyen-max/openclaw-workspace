"""
PocketMind Prompts

System prompts and prompt templates.
"""

from typing import Dict, Optional


# Base system prompt
SYSTEM_PROMPT = """You are PocketMind, a personal AI assistant that lives on your device.
You are helpful, friendly, and respectful.
Your goal is to assist the user with their tasks efficiently.

Key principles:
- Be concise unless detailed responses are requested
- Stay helpful and positive
- Respect user privacy (you don't know anything beyond what they share)
- Admit when you don't know something
- Keep responses conversational
"""


# Prompt with user context (for Day 2+)
def build_personalized_prompt(
    user_name: str = "",
    response_style: str = "casual",
    use_emojis: bool = True,
    context: Optional[Dict] = None
) -> str:
    """
    Build a personalized system prompt with user context.
    
    Args:
        user_name: User's name
        response_style: Response style (brief, detailed, casual, professional)
        use_emojis: Whether to use emojis
        context: Additional context dictionary
        
    Returns:
        Formatted system prompt
    """
    prompt = SYSTEM_PROMPT
    
    # Add user name
    if user_name:
        prompt += f"\nThe user's name is {user_name}."
    
    # Add response style
    if response_style == "brief":
        prompt += "\nKeep responses concise and to the point."
    elif response_style == "detailed":
        prompt += "\nProvide detailed and thorough responses when appropriate."
    elif response_style == "casual":
        prompt += "\nUse a casual, friendly, conversational tone."
    elif response_style == "professional":
        prompt += "\nUse a professional, formal tone."
    
    # Emoji preference
    if not use_emojis:
        prompt += "\nDo not use emojis in your responses."
    
    # Add any additional context
    if context:
        if context.get("schedule_type"):
            prompt += f"\nThe user typically works: {context['schedule_type']}."
        if context.get("timezone"):
            prompt += f"\nThe user's timezone is: {context['timezone']}."
        if context.get("goal"):
            promptThe user's main += f"\n goal: {context['goal']}."
    
    return prompt


# Onboarding prompts
ONBOARDING_WELCOME = """
🤖 Welcome to PocketMind!

I'm your personal AI assistant.
I'll learn about you to help better.

Let's get to know each other...
"""

# Chat prompt template
CHAT_TEMPLATE = """<|system|>
{system_prompt}
</s>
<|user|>
{user_message}
</s>
<|assistant|>
"""


# Example prompts for testing
EXAMPLE_PROMPTS = [
    "Hello, how are you?",
    "What can you help me with?",
    "Tell me a joke.",
    "What's the weather like?",
]


def format_chat_message(role: str, content: str) -> Dict[str, str]:
    """
    Format a message for chat completion.
    
    Args:
        role: Message role (system, user, assistant)
        content: Message content
        
    Returns:
        Message dictionary
    """
    return {"role": role, "content": content}
