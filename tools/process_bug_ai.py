import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def process_bug_with_ai(user_description):
    """
    Uses Groq (gpt-oss-120b) to structure a raw bug description.
    """
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL")
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    prompt = f"""
    You are an expert QA Engineer. Convert the following raw user bug report into a professional Jira ticket.
    
    RAW DESCRIPTION:
    {user_description}
    
    RESPONSE FORMAT (JSON ONLY):
    {{
      "summary": "Concise bug title",
      "description": "Structured markdown with Steps, Expected, and Actual results",
      "priority": "High/Medium/Low"
    }}
    
    RULES:
    1. Do not use conversational filler.
    2. Use professional terminology.
    3. Ensure the description uses Markdown headers (###).
    """
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "response_format": {"type": "json_object"}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            return json.loads(content)
        else:
            print(f"Error from Groq: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Exception in AI processing: {str(e)}")
        return None

if __name__ == "__main__":
    test_desc = "The login button doesn't do anything when I click it on the staging site. I tried Chrome and Safari."
    result = process_bug_with_ai(test_desc)
    print(json.dumps(result, indent=2))
