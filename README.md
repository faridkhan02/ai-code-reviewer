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

## License

This project is provided as-is. Feel free to modify the README and code for your own use.
