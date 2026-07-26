# AI Code Reviewer Platform

Created by **Md Farid Khan**.

A Streamlit-based AI code review application for Python. Upload or paste code and get analysis for bugs, security issues, performance, style, and an AI explanation.

## Project Summary

AI Code Reviewer is designed to help developers quickly identify issues in Python source files. It provides:

- syntax validation and parsing checks
- bug detection for unsafe or risky patterns
- security checks for hardcoded secrets and unsafe functions
- performance hints for loops and expensive operations
- style recommendations to improve readability
- categorized results with guided fixes

## Features

- Upload a `.py` file or paste Python code directly.
- Syntax and parsing validation.
- Bug detection for common Python issues.
- Security checks for unsafe functions, hardcoded secrets, and disabled SSL verification.
- Performance hints for nested loops and large ranges.
- Style checks for long lines, tab usage, and naming conventions.
- Categorized review results with suggested fixes.

## Installation

1. Create a Python virtual environment:

```bash
python -m venv venv
```

2. Activate the environment:

Windows:
```powershell
venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

From the repository root, run:

```bash
streamlit run main.py
```

If you prefer a dedicated entrypoint, use:

```bash
streamlit run run.py
```

## Project Structure

- `app/` - Main app package and UI components.
- `app/main.py` - Streamlit application entrypoint.
- `app/ui.py` - UI rendering and review display code.
- `app/sidebar.py` - Sidebar settings for review options.
- `app/utils.py` - Utility helpers such as CSS loading.
- `app/reviewer.py` - Review orchestration logic.
- `app/services/` - Analysis services for bugs, security, performance, and style.
- `app/static/css/style.css` - Custom application styling.

## Notes

- Make sure the Python environment is active when you run the app.
- If the app cannot find the `app` package, ensure you launch Streamlit from the repository root.
- The review UI is designed for Python code only.

## Author

Md Farid Khan

## API Keys & Configuration

This project integrates with large language models. By default it uses Google's Gemini (Generative AI) SDK, and an OpenAI key can be configured as an alternative for future use.

- Copy `.env.example` to `.env` and set your keys:

```bash
cp .env.example .env
# then edit .env and add your key values
```

- Environment variables supported (set in `.env`):
	- `GEMINI_API_KEY` — required for the default Gemini model integration.
	- `OPENAI_API_KEY` — optional if you plan to use OpenAI in the future.
	- `OLLAMA_BASE_URL` — optional local URL for Ollama if used.
	- `GEMINI_MODEL` — override the Gemini model (defaults are in `app/config/setting.py`).

The app loads these variables via `python-dotenv` in `app/config/setting.py`.

## Usage Example

Run the application from the repository root so Python package imports resolve correctly:

```bash
streamlit run main.py
```

Alternatively use the provided `run.py` launcher:

```bash
streamlit run run.py
```

Open `http://localhost:8501` in your browser.

## Troubleshooting & Solutions

- Issue: `ModuleNotFoundError: No module named 'app'` — Solution: start Streamlit from the repo root (run `streamlit run main.py`), or use `run.py` which configures `sys.path`. Avoid running `streamlit run app/main.py` from inside `app/` unless you add the parent directory to `PYTHONPATH`.

- Issue: `CSS file not found: app/static/css/style.css` — Solution: ensure `app/static/css/style.css` exists and the app is started from the project root. The loader in `app/utils.py` checks `os.path.exists()` using a path built in `app/main.py`.

- Issue: Syntax errors reported for uploaded code — Solution: the analyzer attempts to parse the code with `ast`; fix the indicated syntax error lines in your source and run the review again.

- Issue: Local Git push fails or large binary/venv files included — Solution: ensure `venv/` and other large artifacts are listed in `.gitignore` (this repo includes a `.gitignore`). Do not commit real API keys; use `.env.example` and keep `.env` out of source control.

- If a check fails or you see an unexpected exception in the UI, copy the traceback and open an issue in the project with the traceback and the code sample that reproduced it.

## Contributing

Contributions are welcome. Open issues or pull requests for bug fixes, improvements, and new analysis features.

> Note: this repository does not include a license file. If you plan to reuse or share the code publicly, consider adding a license that matches your needs.
