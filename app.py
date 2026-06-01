import os
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv

from readme_generator import generate_readme, ReadmeGenerationError

load_dotenv()

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/generate")
def api_generate():
    payload = request.get_json(silent=True) or {}
    project_input = (payload.get("project_input") or "").strip()

    if not project_input:
        return jsonify({
            "error": "Please provide a project description, repository summary, or source snippets."
        }), 400

    try:
        readme = generate_readme(project_input)
    except ReadmeGenerationError as exc:
        return jsonify({"error": str(exc)}), 500

    return jsonify({"readme": readme})

@app.post("/generate")
def generate_form():
    project_input = (request.form.get("project_input") or "").strip()

    if not project_input:
        return render_template(
            "index.html",
            error="Please enter a project description, repository summary, or source snippets."
        )

    try:
        readme = generate_readme(project_input)
    except ReadmeGenerationError as exc:
        return render_template("index.html", error=str(exc), project_input=project_input)

    return render_template("index.html", project_input=project_input, readme=readme)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
