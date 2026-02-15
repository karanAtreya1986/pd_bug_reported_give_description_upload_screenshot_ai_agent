import os
import requests
import json
import base64
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

def markdown_to_adf(text):
    """
    Primitive converter for Markdown-like text to Jira Atlassian Document Format (ADF).
    Supports: ### Headers, Bullet points (- or 1.), and standard text.
    """
    lines = text.split('\n')
    content = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Headers (###)
        if line.startswith('###'):
            content.append({
                "type": "heading",
                "attrs": {"level": 3},
                "content": [{"type": "text", "text": line.replace('###', '').strip()}]
            })
        elif line.startswith('##'):
            content.append({
                "type": "heading",
                "attrs": {"level": 2},
                "content": [{"type": "text", "text": line.replace('##', '').strip()}]
            })
        # Bullet points
        elif line.startswith('- ') or line.startswith('* '):
            content.append({
                "type": "bulletList",
                "content": [{
                    "type": "listItem",
                    "content": [{
                        "type": "paragraph",
                        "content": [{"type": "text", "text": line[2:].strip()}]
                    }]
                }]
            })
        # Numbered lists
        elif any(line.startswith(str(i) + '.') for i in range(1, 10)):
            content.append({
                "type": "orderedList",
                "content": [{
                    "type": "listItem",
                    "content": [{
                        "type": "paragraph",
                        "content": [{"type": "text", "text": line[line.find('.')+1:].strip()}]
                    }]
                }]
            })
        # Regular paragraph
        else:
            content.append({
                "type": "paragraph",
                "content": [{"type": "text", "text": line}]
            })
            
    return content

def submit_jira_ticket(ai_data, screenshots_base64=None):
    """
    Submits a bug ticket to Jira and uploads attachments.
    """
    base_url = os.getenv("JIRA_BASE_URL").rstrip('/')
    email = os.getenv("JIRA_EMAIL")
    token = os.getenv("JIRA_API_TOKEN")
    project_key = os.getenv("JIRA_PROJECT_KEY")
    
    auth = HTTPBasicAuth(email, token)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # 1. Create Issue with ADF Description
    adf_content = markdown_to_adf(ai_data.get("description", "No description provided."))
    
    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": ai_data.get("summary", "New Bug Report"),
            "description": {
                "type": "doc",
                "version": 1,
                "content": adf_content
            },
            "issuetype": {"name": "Bug"},
            "priority": {"name": ai_data.get("priority", "Medium")},
            "labels": ["AI-Generated", "Ticket-Pilot"]
        }
    }

    print(f"Creating Jira issue in project {project_key}...")
    response = requests.post(f"{base_url}/rest/api/3/issue", json=payload, auth=auth, headers=headers)
    
    if response.status_code != 201:
        print(f"Failed to create issue: {response.status_code}")
        print(response.text)
        return None

    issue_data = response.json()
    issue_key = issue_data.get("key")
    print(f"✅ Issue Created: {issue_key}")

    # 2. Upload Attachments
    if screenshots_base64:
        if not os.path.exists(".tmp"):
            os.makedirs(".tmp")
            
        print(f"Uploading {len(screenshots_base64)} attachments...")
        for i, b64_str in enumerate(screenshots_base64):
            try:
                if "," in b64_str:
                    b64_str = b64_str.split(",")[1]
                
                img_data = base64.b64decode(b64_str)
                file_path = f".tmp/screenshot_{i}.png"
                
                with open(file_path, "wb") as f:
                    f.write(img_data)
                
                attach_headers = {"X-Atlassian-Token": "no-check"}
                with open(file_path, "rb") as f:
                    files = {"file": (f"screenshot_{i}.png", f, "image/png")}
                    attach_url = f"{base_url}/rest/api/3/issue/{issue_key}/attachments"
                    attach_res = requests.post(attach_url, files=files, auth=auth, headers=attach_headers)
                    
                    if attach_res.status_code == 200:
                        print(f"  - Attachment {i} uploaded successfully.")
            except Exception as e:
                print(f"  - Error processing attachment {i}: {str(e)}")

    return {"key": issue_key, "url": f"{base_url}/browse/{issue_key}"}

if __name__ == "__main__":
    test_ai_data = {
        "summary": "Sample AI Bug with ADF",
        "description": "### Summary\nTest bug\n\n### Steps\n1. Open app\n2. Click button\n\n- Some point",
        "priority": "Medium"
    }
    submit_jira_ticket(test_ai_data)
