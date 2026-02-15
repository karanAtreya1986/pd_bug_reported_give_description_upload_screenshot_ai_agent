# 🗺️ Jira Ticket Pilot: Technical Blueprint

## 🔄 System Data Flow

1.  **Frontend (UI):**
    - User enters a bug description.
    - User uploads screenshot(s).
    - Frontend packages this into an "Origin Payload".

2.  **AI Orchestration (`tools/process_bug_ai.py`):**
    - **Input:** Origin Payload (Text + Base64 Images).
    - **Logic:** Calls Groq API (`gpt-oss-120b`).
    - **Output:** A structured "Ticket Draft" (JSON) containing:
        - `summary`: A concise bug title.
        - `description`: A detailed report with "Steps to Reproduce", "Expected", and "Actual".
        - `priority`: AI-suggested priority (Low/Medium/High/Highest).

3.  **Jira Integration (`tools/submit_jira_ticket.py`):**
    - **Step A:** Creates the Jira issue using the Ticket Draft.
    - **Step B:** Retrieves the `issue_id`.
    - **Step C:** Iterates through screenshots and uploads them to the `issue_id` via `/attachments` endpoint.
    - **Output:** Final Jira URL/Key.

4.  **User Loop:**
    - UI receives the Jira Key.
    - Displays a "Success" toast with a link.

---

## 🛠️ Technology Stack
- **Frontend:** Vanilla JS / Vite (Premium CSS).
- **Backend/Tools:** Python 3.x (Requests, Groq-SDK).
- **LLM:** Groq (`openai/gpt-oss-120b`).
- **Storage:** `.tmp/` for ephemeral image processing.

---

## 🔐 Security & Auth
- Credentials stored in `.env`.
- `X-Atlassian-Token: no-check` header used for attachment uploads.
