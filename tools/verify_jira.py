import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

def verify_jira():
    url = f"{os.getenv('JIRA_BASE_URL')}/rest/api/3/myself"
    auth = HTTPBasicAuth(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
    
    headers = {
        "Accept": "application/json"
    }

    print(f"Connecting to Jira at {url}...")
    try:
        response = requests.request("GET", url, headers=headers, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            print(f"✅ Jira Connected! Authenticated as: {user_data.get('displayName')}")
            return True
        else:
            print(f"❌ Jira Connection Failed: {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    verify_jira()
