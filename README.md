# README Generator AI

A fast Flask app that turns a short project description, source summary, or repository notes into a polished `README.md`.

## Features

- Web form and JSON API
- OpenAI Responses API integration
- Markdown-only output
- Simple, deployable Flask structure
- Works well as a GitHub portfolio project

## Project structure

```text
readme-generator-ai/
├── app.py
├── readme_generator.py
├── requirements.txt
├── .env.example
├── README.md
├── templates/
│   └── index.html
└── static/
    └── styles.css
```

## Prerequisites

- Python 3.10 or newer
- An OpenAI API key saved as `OPENAI_API_KEY`

The OpenAI Python SDK reads the API key from the environment, and the current SDK reference uses the Responses API for text generation.

## Setup

```bash
git clone https://github.com/yourusername/readme-generator-ai.git
cd readme-generator-ai
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your key:

```bash
cp .env.example .env
```

## Run

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## API

### POST /api/generate

Request body:

```json
{
  "project_input": "A Flask task tracker with SQLite, CRUD routes, and JWT login."
}
```

Response:

```json
{
  "readme": "# Project Title\n..."
}
```

## Tips

- Provide a short but specific project summary for the best result.
- Add stack details, routes, and features in the input whenever possible.
- Set `OPENAI_MODEL` in `.env` if you want to change the model name.

## Roadmap

- Repository URL import
- Automatic file tree analysis
- Badge generation
- Mermaid architecture diagrams
- One-click publish to GitHub

## Licence

MIT
