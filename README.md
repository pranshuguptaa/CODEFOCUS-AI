# CodeFocus AI

CodeFocus AI is a web application that analyzes Slack messages and Git commits to provide actionable insights and task management for development teams. It uses Natural Language Processing (NLP) to extract meaningful information from communication channels and version control systems.

## Features

- **Slack Message Analysis**: Automatically summarizes Slack messages to identify actionable items and updates
- **Git Commit Analysis**: Parses Git commits to generate relevant tasks and review items
- **Real-time Processing**: Provides instant analysis of communication and code changes
- **Web Interface**: User-friendly dashboard to view summaries and tasks

## Tech Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS
- **NLP**: spaCy (English language model)
- **Version Control**: Git

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pranshuguptaa/CODEFOCUS-AI.git
cd CODEFOCUS-AI
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install flask spacy
python -m spacy download en_core_web_sm
```

## Usage

1. Start the Flask application:
```bash
python codefocus/app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. The application will process:
   - Slack messages from `slack_sample.txt`
   - Git commits from `git_sample.txt`

## Project Structure

```
codefocus/
  ├── app.py         # Backend logic
  ├── static/        # CSS, JS
  │   └── style.css
  ├── templates/     # HTML
  │   └── index.html
  ├── slack_sample.txt
  └── git_sample.txt
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- spaCy for NLP capabilities
- Flask for the web framework
- All contributors who help improve this project 