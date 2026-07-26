"""
UI Components
"""

import streamlit as st


def page_header():
    st.markdown(
        """
        <div class="section-header">
            <h2>Upload your Python code or paste it below</h2>
            <p>Get fast AI-driven feedback on bugs, security, performance, style, and explanation.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def upload_code_ui():
    page_header()

    option = st.radio(
        "Choose input mode",
        ["Upload File", "Paste Code"],
        horizontal=True,
    )

    code = ""

    if option == "Upload File":
        uploaded_file = st.file_uploader(
            "Upload Python file",
            type=["py"],
            help="Select a .py file to analyze.",
        )

        if uploaded_file:
            code = uploaded_file.read().decode("utf-8")
    else:
        code = st.text_area(
            "Paste Python code",
            height=320,
            placeholder="def hello_world():\n    print(\"Hello world\")",
        )

    if code:
        with st.expander("Code preview", expanded=True):
            st.code(code, language="python")

    return code


# Category metadata: icon, label, severity, and a short description of what the section means
_CATEGORY_META = {
    "bugs": {
        "title": "Bug Detection",
        "icon": "🐞",
        "severity": "warning",
        "description": "Logic problems, invalid control flow, and runtime-risk code.",
    },
    "security": {
        "title": "Security Analysis",
        "icon": "🔒",
        "severity": "error",
        "description": "Potential vulnerabilities, unsafe patterns, and hard-coded secrets.",
    },
    "performance": {
        "title": "Performance Analysis",
        "icon": "⚡",
        "severity": "info",
        "description": "Slow or heavy code patterns that can be optimized.",
    },
    "style": {
        "title": "Style Analysis",
        "icon": "🎨",
        "severity": "success",
        "description": "Readability, formatting, and Python style guideline suggestions.",
    },
}


def _render_summary_stats(analysis):
    stats = [
        ("Syntax", analysis.get("syntax", "N/A")),
        ("Functions", analysis.get("functions", 0)),
        ("Classes", analysis.get("classes", 0)),
        ("Imports", analysis.get("imports", 0)),
        ("Variables", analysis.get("variables", 0)),
    ]

    cols = st.columns(len(stats))
    for col, (label, value) in zip(cols, stats):
        col.metric(label, value)


def _suggest_fix(issue):
    if "Try block without except" in issue:
        return "Add an except handler or an else/finally block to catch failures safely."
    if "Generic except detected" in issue:
        return "Use specific exception types instead of bare except to avoid hiding bugs."
    if "Unsafe function detected" in issue:
        return "Avoid eval/exec or replace with safe parsing and controlled execution."
    if "Hardcoded password" in issue:
        return "Move secrets to environment variables or a secure vault."
    if "Hardcoded API Key" in issue:
        return "Store API keys outside source code and read them at runtime."
    if "SSL verification disabled" in issue:
        return "Re-enable SSL verification or use a trusted certificate."
    if "Nested loop detected" in issue:
        return "Refactor the loops or use more efficient data processing techniques."
    if "Large range loop detected" in issue:
        return "Avoid huge loops or break the work into smaller chunks or vectorized operations."
    if "Line" in issue and "exceeds 88 characters" in issue:
        return "Wrap long lines to improve readability and follow PEP 8."
    if "contains tab indentation" in issue:
        return "Use spaces for indentation to keep style consistent."
    if "Variable naming may not follow snake_case" in issue:
        return "Rename variables using snake_case for better Python style."
    return "Review the issue and update the code accordingly."


def _render_review_section(title, icon, items, description, severity):
    st.markdown(
        f"""
        <div class="section-card section-card--{severity}">
            <div class="section-card-header">
                <div class="section-card-title">{icon} {title}</div>
                <div class="section-card-badge">{len(items)}</div>
            </div>
            <div class="section-card-description">{description}</div>
        """,
        unsafe_allow_html=True,
    )

    if not items:
        st.markdown(
            "<div class='section-card-body'><div class='section-card-empty'>No issues found.</div></div></div>",
            unsafe_allow_html=True,
        )
        return

    issues_html = "".join(
        f"""
        <div class='issue-row'>
            <div class='issue-text'>• {item}</div>
            <div class='issue-fix'>Suggestion: {_suggest_fix(item)}</div>
        </div>
        """
        for item in items
    )

    st.markdown(
        f"""
        <div class='section-card-body'>
            {issues_html}
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def display_review(result):
    st.markdown("## 🤖 AI Review Report")

    analysis = result.get("analysis", {})
    errors = analysis.get("errors", [])

    if errors:
        st.markdown(
            """
            <div class='error-card'>
                <div class='error-card-title'>❗ Syntax & Parsing Errors</div>
            """,
            unsafe_allow_html=True,
        )
        for error in errors:
            st.markdown(
                f"<div class='error-message'>{error}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<div class='error-fix'>Suggested fix: Fix the syntax issue and re-run the review.</div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("---")

    st.markdown("### 🔎 Review Summary")
    st.markdown(
        "<div class='summary-intro'>This section shows the main review findings and the issue cards below show what the problem is and how to fix it.</div>",
        unsafe_allow_html=True,
    )

    _render_summary_stats(analysis)
    st.markdown("---")

    for key, meta in _CATEGORY_META.items():
        _render_review_section(
            meta["title"],
            meta["icon"],
            analysis.get(key, []),
            meta["description"],
            meta["severity"],
        )

    st.markdown("---")
    st.markdown("### 💡 AI Explanation")
    explanation = result.get("explanation", "").strip()
    st.write(explanation or "No explanation available.")