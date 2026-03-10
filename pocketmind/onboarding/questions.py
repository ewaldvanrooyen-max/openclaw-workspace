"""
PocketMind Onboarding Questions

The 7 questions asked during onboarding to build user profile.
"""

from typing import Dict, List, Callable, Optional
from dataclasses import dataclass


@dataclass
class Question:
    """Represents a single onboarding question."""
    id: str
    text: str
    options: Optional[List[str]] = None
    input_type: str = "text"  # text, choice, date, multi
    required: bool = True
    skip_option: Optional[str] = None
    follow_ups: Optional[Dict] = None


class OnboardingQuestions:
    """
    The 7-question onboarding flow for PocketMind.
    
    Q1: Name
    Q2: Main goal
    Q3: Schedule type
    Q4: Timezone
    Q5: Important dates
    Q6: Response style
    Q7: Additional context
    """
    
    # Goal options
    GOALS = [
        "Productivity & tasks",
        "Learning & research",
        "Creative writing",
        "Personal organization",
        "Just curious / general chat"
    ]
    
    # Schedule options
    SCHEDULES = [
        "9-5 office worker",
        "Shift work",
        "Self-employed / flexible",
        "Student",
        "Retired"
    ]
    
    # Response style options
    RESPONSE_STYLES = [
        "Brief & to the point",
        "Detailed & thorough",
        "Casual & friendly",
        "Professional & formal"
    ]
    
    # Common timezones
    COMMON_TIMEZONES = [
        "Africa/Johannesburg",
        "Africa/Cairo",
        "Africa/Lagos",
        "Europe/London",
        "Europe/Paris",
        "Europe/Berlin",
        "America/New_York",
        "America/Chicago",
        "America/Denver",
        "America/Los_Angeles",
        "Asia/Dubai",
        "Asia/Singapore",
        "Asia/Tokyo",
        "Australia/Sydney",
        "UTC"
    ]
    
    @classmethod
    def get_all_questions(cls) -> List[Question]:
        """Get all 7 onboarding questions."""
        return [
            Question(
                id="name",
                text="What should I call you?",
                input_type="text",
                required=True
            ),
            Question(
                id="goal",
                text="What's your main goal for having me?",
                options=cls.GOALS,
                input_type="choice",
                required=True
            ),
            Question(
                id="schedule",
                text="What's your typical schedule?",
                options=cls.SCHEDULES,
                input_type="choice",
                required=False,
                skip_option="I'll tell you later"
            ),
            Question(
                id="timezone",
                text="What time zone are you in?",
                options=cls.COMMON_TIMEZONES,
                input_type="choice",
                required=True
            ),
            Question(
                id="important_dates",
                text="Any important dates to remember? (birthdays, anniversaries, deadlines)",
                input_type="text",
                required=False,
                skip_option="Skip for now"
            ),
            Question(
                id="response_style",
                text="How do you prefer I respond?",
                options=cls.RESPONSE_STYLES,
                input_type="choice",
                required=True
            ),
            Question(
                id="additional_context",
                text="Anything else I should know about you?",
                input_type="text",
                required=False,
                skip_option="That's enough"
            )
        ]
    
    @classmethod
    def get_question(cls, question_id: str) -> Optional[Question]:
        """Get a specific question by ID."""
        questions = cls.get_all_questions()
        for q in questions:
            if q.id == question_id:
                return q
        return None
    
    @classmethod
    def build_profile(cls, answers: Dict) -> Dict:
        """
        Build a user profile from onboarding answers.
        
        Args:
            answers: Dictionary of question_id -> answer
            
        Returns:
            Complete user profile dictionary
        """
        # Map answer to response style
        response_style = answers.get("response_style", "")
        if "brief" in response_style.lower():
            detail_level = "brief"
            tone = "direct"
        elif "detailed" in response_style.lower():
            detail_level = "detailed"
            tone = "informative"
        elif "casual" in response_style.lower():
            detail_level = "medium"
            tone = "friendly"
        elif "professional" in response_style.lower():
            detail_level = "medium"
            tone = "formal"
        else:
            detail_level = "medium"
            tone = "neutral"
        
        # Parse important dates if provided
        important_dates = []
        dates_text = answers.get("important_dates", "")
        if dates_text and dates_text.strip():
            # Simple parsing - split by commas or newlines
            for date_str in dates_text.replace("\n", ",").split(","):
                date_str = date_str.strip()
                if date_str:
                    important_dates.append({
                        "name": date_str,
                        "raw": date_str
                    })
        
        # Build profile
        profile = {
            "name": answers.get("name", "").strip(),
            "goal": cls._normalize_goal(answers.get("goal", "")),
            "goal_display": answers.get("goal", ""),
            "schedule_type": answers.get("schedule", "").lower().replace(" ", "_"),
            "schedule_display": answers.get("schedule", ""),
            "timezone": answers.get("timezone", "UTC"),
            "response_style": response_style,
            "detail_level": detail_level,
            "tone": tone,
            "important_dates": important_dates,
            "personal_context": {
                "notes": answers.get("additional_context", "")
            },
            "preferences": {
                "use_emojis": True,
                "include_greetings": True
            }
        }
        
        return profile
    
    @classmethod
    def _normalize_goal(cls, goal: str) -> str:
        """Normalize goal string to key."""
        goal_lower = goal.lower()
        if "productivity" in goal_lower:
            return "productivity"
        elif "learning" in goal_lower or "research" in goal_lower:
            return "learning"
        elif "creative" in goal_lower:
            return "creative"
        elif "organization" in goal_lower:
            return "organization"
        else:
            return "general"


def format_profile_summary(profile: Dict) -> str:
    """
    Format a human-readable summary of the user profile.
    
    Args:
        profile: User profile dictionary
        
    Returns:
        Formatted summary string
    """
    lines = []
    lines.append(f"• Your name: {profile.get('name', 'Unknown')}")
    lines.append(f"• Main goal: {profile.get('goal_display', 'Not specified')}")
    
    if profile.get('schedule_display'):
        lines.append(f"• Schedule: {profile.get('schedule_display')}")
    
    lines.append(f"• Timezone: {profile.get('timezone', 'UTC')}")
    lines.append(f"• Response style: {profile.get('response_style', 'Medium')}")
    
    dates = profile.get('important_dates', [])
    if dates:
        lines.append(f"• Important dates: {len(dates)} saved")
    
    notes = profile.get('personal_context', {}).get('notes', '')
    if notes:
        lines.append(f"• Notes: {notes[:50]}...")
    
    return "\n".join(lines)
