# 🤖 SOP: AI Bug Processing (Groq gpt-oss-120b)

## 🎯 Goal
Transform raw user input and visual evidence into a structured, professional Jira bug report.

## 📥 Inputs
- `description`: Raw text from the user.
- `screenshots`: (Optional) Metadata or OCR from images if available (Note: `gpt-oss-120b` is text-centric; we will mainly use description but allow future vision expansion).

## 🧠 Prompt Strategy
The AI must follow this strict template for the description:

```markdown
### 📝 Summary
[A concise, 1-sentence bug title]

### 🔄 Steps to Reproduce
1. [Step 1]
2. [Step 2]
...

### 🎯 Expected Result
[What should happen]

### ❌ Actual Result
[What actually happened]

### 🛠️ Environment Info
- Platform: [Inferred if possible]
- Added via: Jira Ticket Pilot
```

## 📤 Output Format
A JSON object matching the Jira REST API v3 schema:
```json
{
  "summary": "...",
  "description": "...",
  "priority": "High/Medium/Low"
}
```

## ⚠️ Edge Cases
- **No Description:** If the user provides only images, prompt them for context or infer from image filenames.
- **Vague Input:** AI should attempt to expand common terms (e.g., "login broke" -> "User is unable to authenticate via the login page").
