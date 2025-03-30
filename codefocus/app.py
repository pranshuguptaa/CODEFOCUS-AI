from flask import Flask, render_template, jsonify
import spacy

# Initialize Flask app
app = Flask(__name__)

# Load spaCy NLP model (small English model)
nlp = spacy.load('en_core_web_sm')

# Function to summarize Slack messages
def summarize_slack(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()
        doc = nlp(text)
        actions = []
        # Look for sentences with actionable keywords
        for sent in doc.sents:
            if any(keyword in sent.text.lower() for keyword in ["working", "fixed", "stuck"]):
                actions.append(sent.text.strip())
        return actions if actions else ["No actionable updates found."]
    except FileNotFoundError:
        return ["Error: Slack data file not found."]

# Function to parse Git commits and assign tasks
def parse_git(file_path):
    try:
        with open(file_path, 'r') as f:
            commits = f.readlines()
        tasks = []
        for commit in commits:
            commit = commit.strip()
            if "fix" in commit.lower():
                task_desc = commit.split('-')[1].strip() if '-' in commit else commit
                tasks.append(f"Test {task_desc}")
            elif "add" in commit.lower():
                task_desc = commit.split('-')[1].strip() if '-' in commit else commit
                tasks.append(f"Review {task_desc}")
        return tasks if tasks else ["No tasks generated from commits."]
    except FileNotFoundError:
        return ["Error: Git data file not found."]

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to process data and return JSON
@app.route('/process')
def process():
    slack_summary = summarize_slack('slack_sample.txt')
    git_tasks = parse_git('git_sample.txt')
    # Return results as JSON for frontend
    return jsonify({
        'summary': slack_summary,
        'tasks': git_tasks
    })

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)