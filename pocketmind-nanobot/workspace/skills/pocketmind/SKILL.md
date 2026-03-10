# PocketMind Skill 🧠

Personal AI memory assistant with 7-question onboarding system.

## Trigger Phrases

- "onboard me"
- "get to know me"
- "remember me"
- "setup profile"
- "initialize"
- First message with greeting (if no user profile exists)

## Description

PocketMind uses a friendly 7-question onboarding process to learn about you. Your answers are saved to `memory/user-profile.md` and used to personalize all interactions.

The onboarding questions:

1. **Name**: What should I call you?
2. **Goal**: What's your main goal for having me? (Productivity, learning, creative, organization, or chat)
3. **Schedule**: What's your typical schedule? (9-5, shift, flexible, student, retired)
4. **Timezone**: What timezone are you in?
5. **Important Dates**: Any important dates to remember? (birthdays, anniversaries, deadlines)
6. **Response Style**: How do you prefer I respond? (Brief, detailed, casual, professional)
7. **Additional Context**: Anything else I should know about you?

## Behavior

### Onboarding Flow

When triggered, PocketMind will:
1. Check if a user profile already exists in `memory/user-profile.md`
2. If no profile exists, start the 7-question onboarding
3. Ask one question at a time for a conversational experience
4. Save all answers to `memory/user-profile.md`
5. Confirm the profile has been saved
6. Summarize what it learned

### Profile Verification

On startup, PocketMind will:
1. Check for existing profile in `memory/user-profile.md`
2. If found, load and use it for personalization
3. If not found and user starts chatting, trigger onboarding

### Updating Profile

User can update their profile at any time by:
- Saying "update my profile"
- Saying "change my preferences"
- Editing `memory/user-profile.md` directly

## Files Used

- `memory/user-profile.md` - Stores all user information
- `memory/conversations/` - Stores conversation history

## Example Onboarding Session

```
PocketMind: Hi! I'm PocketMind, your personal AI memory assistant. 
I'd love to get to know you better! Let me ask you a few questions.

First: What should I call you?

User: You can call me Alex

PocketMind: Great to meet you, Alex! 

Second: What's your primary goal for having an AI assistant?

User: I want help organizing my work and remembering important things

PocketMind: That's helpful to know! 

Third: What tasks do you want me to help with most?
```

## Integration

This skill works alongside Nanobot's built-in memory system. The user profile is loaded at the start of each conversation and used to personalize responses.

## Notes

- Questions can be answered in any order by saying "let me skip ahead"
- Users can answer multiple questions at once
- Partial answers are saved immediately
- Profile is read at the start of each conversation
