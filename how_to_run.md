# 🚀 Jira Ticket Pilot: How to Run

This project is designed to run as a silent background service on your Windows machine. You do not need to use the terminal to start the application.

## 🛠️ Automated Background Service
The application has been configured to start automatically in the background every time you log into Windows. 

### 1. Primary Access (Link)
Simply open your browser and go to:
**[http://localhost:5000](http://localhost:5000)**

### 2. Manual Start (If ever needed)
If you ever want to launch the UI manually and ensure the server is up:
- Double-click the **`Jira_Ticket_Pilot`** shortcut in the project folder.
- Or, double-click **`run_silently.vbs`**.

### 3. Stopping the Service
Since the server runs silently in the background:
- Open **Task Manager** (Ctrl+Shift+Esc).
- Find the **python.exe** process running the server.
- Click **End Task**.

---

## 📂 Project Structure
- `index.html`: The premium bug reporting interface.
- `server.py`: The backend bridge.
- `tools/`: Python scripts for Groq AI and Jira API integration.
- `run_silently.vbs`: The script that hides the terminal window.
- `.env`: Your secure API keys and credentials.

## 📝 Features & Protocol
- **AI Processing**: Raw descriptions are professionally structured by Groq LLM.
- **Visual Evidence**: Multiple screenshots are supported and automatically attached to Jira issues.
- **Professional Formatting**: Tickets use Atlassian Document Format (ADF) for a premium look in Jira.
