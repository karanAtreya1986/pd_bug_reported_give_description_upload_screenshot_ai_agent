import os
import requests
from dotenv import load_dotenv

load_dotenv()

def verify_groq():
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL")
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": "Hello, are you online? Answer with 'Ready' only if you are."}
        ],
        "max_tokens": 10
    }

    print(f"Connecting to Groq using model {model}...")
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            answer = result['choices'][0]['message']['content']
            print(f"✅ Groq Connected! Response: {answer}")
            return True
        else:
            print(f"❌ Groq Connection Failed: {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    verify_groq()
