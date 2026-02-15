<<<<<<< HEAD
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
=======
# 🚀 Jira Ticket Pilot: Setup & Run Guide (Any Machine)

Follow these steps to set up the Jira Ticket Pilot on any Windows machine.

## 📦 1. Installation
Ensure you have **Python 3.10+** installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

## � 2. Configuration
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

## � 5. Stopping the Server
Since the server runs as a background Python process:
1. Open **Task Manager** (Ctrl+Shift+Esc).
2. End the **Python** process.
>>>>>>> dbbb4f3
