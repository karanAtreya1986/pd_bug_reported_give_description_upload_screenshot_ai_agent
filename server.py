import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from tools.process_bug_ai import process_bug_with_ai
from tools.submit_jira_ticket import submit_jira_ticket

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/submit-bug', methods=['POST'])
def handle_submit_bug():
    data = request.json
    description = data.get('description')
    screenshots = data.get('screenshots', [])

    if not description:
        return jsonify({"error": "Description is required"}), 400

    # 1. Process with AI
    print(f"Processing bug with AI: {description[:50]}...")
    ai_result = process_bug_with_ai(description)
    
    if not ai_result:
        return jsonify({"error": "AI processing failed"}), 500

    # 2. Submit to Jira
    print("Submitting to Jira...")
    jira_result = submit_jira_ticket(ai_result, screenshots)

    if not jira_result:
        return jsonify({"error": "Jira submission failed"}), 500

    return jsonify(jira_result)

if __name__ == '__main__':
    # Ensure .tmp exists
    if not os.path.exists('.tmp'):
        os.makedirs('.tmp')
    
    print("🚀 Jira Ticket Pilot server running at http://localhost:5000")
    app.run(port=5000, debug=True)
