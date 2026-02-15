# 🚀 Jira Ticket Pilot: Setup & Run Guide (Any Machine)

Follow these steps to set up the Jira Ticket Pilot on any Windows machine.

## 📦 1. Installation
Ensure you have **Python 3.10+** installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🔑 2. Configuration
The project requires a `.env` file to store your credentials safely.
1. Copy `.env.example` and rename it to `.env`.
2. Fill in your **Jira** and **Groq** credentials:
   - `JIRA_BASE_URL`: Your Atlassian domain.
   - `JIRA_API_TOKEN`: Generated from Atlassian security settings.
   - `GROQ_API_KEY`: Your key from Groq Cloud.

## 🚀 3. Running the Application

### Option A: Portable One-Click (Hidden Console)
Double-click **`run_silently.vbs`**. 
- This will launch the backend server invisibly and open the UI at `http://localhost:5000`.

### Option B: Development Mode (Visible Console)
Run the following in your terminal:
```bash
python server.py
```

## 📂 4. Portability Features
- **Relative Paths**: All scripts (`.vbs`, `.bat`, and `.py`) are now designed to detect their own directory. You can move the project folder anywhere.
- **Background Startup**: To make it start with Windows on any machine, copy a shortcut of `run_silently.vbs` into your `shell:startup` folder.

## 🛑 5. Stopping the Server
Since the server runs as a background Python process:
1. Open **Task Manager** (Ctrl+Shift+Esc).
2. End the **Python** process.
