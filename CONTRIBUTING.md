# Contributing to PocketPal 🐺

> *"Alone we can do so little; together we can do so much." — Helen Keller*

Thank you for wanting to contribute! Whether you're a developer, designer, tester, or just someone with a great idea — **you belong here.**

---

## 🎯 How You Can Help

| Way to Contribute | What It Looks Like |
|-------------------|-------------------|
| 🐛 **Bug Reports** | Found something broken? Tell us! |
| 💡 **Feature Ideas** | Got a vision? Share it. |
| 📖 **Documentation** | Help others understand PocketPal |
| 💻 **Code** | Build features, fix bugs, optimize |
| 🧪 **Testing** | Break things before users do |
| 🌐 **Translation** | Add new languages |
| 🎨 **Design** | UI/UX, branding, visuals |
| 📣 **Spread the Word** | Tell friends about PocketPal |

---

## 🚀 Quick Start for Developers

### 1. Fork the Repo

```bash
git clone https://github.com/ewaldvanrooyen-max/pocketmind-agentmesh.git
cd pocketmind-agentmesh
```

### 2. Create a Branch

```bash
git checkout -b feature/your-awesome-feature
# or
git checkout -b fix/something-broken
```

### 3. Make Your Changes

- Follow the code style (we use standard conventions)
- Add comments for complex logic
- Test your changes!

### 4. Submit a Pull Request

```bash
git add .
git commit -m "Add: Your awesome feature"
git push origin feature/your-awesome-feature
```

Then open a PR on GitHub. We'll review it ASAP!

---

## 📋 Coding Standards

### General

- **Be kind** — This is a compassionate project
- **Write readable code** — Clarity > cleverness
- **Comment tricky parts** — Future you will thank you
- **Test your changes** — Don't break things

### Naming Conventions

```python
# Functions: snake_case, descriptive
def calculate_monthly_budget():
    ...

# Classes: PascalCase
class FinancialGuardian:
    ...

# Constants: SCREAMING_SNAKE_CASE
MAX_MEMORY_SIZE = 50 * 1024 * 1024
```

### Git Commits

Use clear, action-based messages:

```
Add: Ghostwriter nanobot for tonal mimicry
Fix: Memory leak in SQLite handler
Update: README with installation steps
Refactor: Router intent classification logic
```

---

## 🧪 Testing Guide

### Running Tests

```bash
# Run all tests
./test.sh

# Run specific module
python -m pytest tests/nanobots/
```

### What to Test

- ✅ Does the feature work as documented?
- ✅ Does it handle edge cases?
- ✅ Does it break existing functionality?
- ✅ Does it respect privacy (no data leaks)?

---

## 🐛 Reporting Bugs

When you find a bug, include:

1. **What you were doing** — Steps to reproduce
2. **What happened** — Error message or unexpected behavior
3. **What you expected** — What should have happened
4. **Device/Environment** — Phone model, OS, Termux version

**Template:**

```markdown
## Bug Description
[Clear description of the issue]

## Steps to Reproduce
1. First step
2. Second step
3. Third step

## Expected Result
[What should happen]

## Actual Result
[What actually happened]

## Environment
- Device: 
- OS: 
- Version: 
```

---

## 💡 Suggesting Features

We love ideas! Before submitting:

1. **Search existing issues** — Maybe it's already suggested
2. **Think about impact** — Does this help many users?
3. **Consider privacy** — No data collection without consent

**Template:**

```markdown
## Feature Idea
[What you're proposing]

## Why It Matters
[How it helps users]

## Possible Approach
[Any ideas on implementation?]
```

---

## 🌐 Translation Guide

Want to add a new language? Here's how:

1. Check `locales/` for existing translations
2. Create a new file: `locales/{language-code}.json`
3. Translate the strings
4. Add the language to the onboarding flow
5. Submit a PR!

### Supported Language Codes

- `en` — English
- `af` — Afrikaans
- `zu` — Zulu
- `xh` — Xhosa
- `st` — Sotho

---

## 📞 Getting Help

- **GitHub Issues** — For bugs and feature requests
- **Discussions** — For questions and ideas
- **Discord** — (Coming soon!)

---

## 🏆 Contributors

Thank you to everyone who's built PocketPal with us!

<!-- Add yourself here when you contribute -->
- **WolfPack Empire** — Core team 🐺

---

## 📜 Code of Conduct

### Our Pledge

We welcome everyone. We're kind, inclusive, and respectful.

### Standards

- ✅ Be welcoming and inclusive
- ✅ Be respectful of different viewpoints
- ✅ Accept constructive criticism gracefully
- ✅ Focus on what's best for the community

### Unacceptable

- ❌ Harassment of any kind
- ❌ Personal attacks
- ❌ Spam or trolling
- ❌ Collecting user data without consent

---

## 🔒 Security & Privacy

When contributing, remember:

- **Never** send user data to external servers
- **Always** use local storage by default
- **Never** log sensitive information
- **Always** sanitize PII in logs

---

## 🙏 Thank You

You're helping build something meaningful. Every bug fix, every feature, every translation — it matters.

**Welcome to the pack!** 🐺

---

*Made with ❤️ by WolfPack Empire*
