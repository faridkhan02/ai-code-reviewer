import os
import sys
import streamlit as st

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app.sidebar import render_sidebar
from app.ui import upload_code_ui, display_review
from app.utils import load_css
from app.reviewer import review_code


def main():
    st.set_page_config(
        page_title="AI Code Reviewer",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    css_path = os.path.join(os.path.dirname(__file__), "static", "css", "style.css")
    load_css(css_path)

    settings = render_sidebar()
    apply_theme(settings.get("theme", "Dark"))

    render_header()

    code = upload_code_ui()

    if not code:
        st.info("Upload a Python file or paste code below to begin the review.")

    col1, col2 = st.columns([1, 5])
    with col1:
        review_button = st.button(
            "▶ Run Review",
            type="primary",
            disabled=not bool(code),
            use_container_width=True,
        )

    if review_button:
        with st.spinner("Analyzing your code — checking bugs, security, performance, and style..."):
            result = review_code(code, settings)

        display_review(result)


def render_header():
    """Render a polished, card-style hero header."""
    st.markdown(
        """
        <div class="app-header">
            <div class="app-header-icon">🤖</div>
            <div class="app-header-text">
                <h1>AI Code Reviewer</h1>
                <p>Upload Python code or paste it below for a detailed review covering
                bugs, security, performance, style, and clear explanations.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def apply_theme(theme: str):
    """Inject theme CSS variables and refined component styling for light or dark mode."""
    if theme == "Dark":
        palette = """
            --bg: #0b1120;
            --fg: #e5e9f0;
            --panel: #0f172a;
            --surface: #151f32;
            --border: rgba(148, 163, 184, 0.16);
            --card: #111a2e;
            --header: #f8fafc;
            --muted: #94a3b8;
            --accent: #2dd4bf;
            --accent-soft: rgba(45, 212, 191, 0.12);
            --info-bg: rgba(56, 189, 248, 0.10);
            --success-bg: rgba(34, 197, 94, 0.10);
            --warning-bg: rgba(245, 158, 11, 0.12);
            --error-bg: rgba(239, 68, 68, 0.12);
            --shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        """
    else:
        palette = """
            --bg: #f8fafc;
            --fg: #1e293b;
            --panel: #ffffff;
            --surface: #ffffff;
            --border: rgba(15, 23, 42, 0.08);
            --card: #ffffff;
            --header: #0f172a;
            --muted: #64748b;
            --accent: #0f766e;
            --accent-soft: rgba(15, 118, 110, 0.08);
            --info-bg: rgba(219, 234, 254, 0.55);
            --success-bg: rgba(220, 252, 231, 0.55);
            --warning-bg: rgba(254, 240, 138, 0.5);
            --error-bg: rgba(254, 202, 202, 0.5);
            --shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        """

    st.markdown(
        f"""
        <style>
            :root {{
                {palette}
            }}

            html, body, [class*="css"] {{
                font-family: "Inter", "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif;
            }}

            .main, .block-container, .appview-container {{
                background-color: var(--bg) !important;
                color: var(--fg) !important;
            }}

            .block-container {{
                padding-top: 2rem;
                padding-bottom: 3rem;
                max-width: 1100px;
            }}

            section[data-testid="stSidebar"] {{
                background-color: var(--panel) !important;
                color: var(--fg) !important;
                border-right: 1px solid var(--border);
            }}

            /* Hero header */
            .app-header {{
                display: flex;
                align-items: center;
                gap: 1.25rem;
                background: linear-gradient(135deg, var(--card) 0%, var(--surface) 100%);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 1.75rem 2rem;
                margin-bottom: 1.75rem;
                box-shadow: var(--shadow);
            }}

            .app-header-icon {{
                font-size: 2.75rem;
                line-height: 1;
                background: var(--accent-soft);
                border-radius: 14px;
                padding: 0.6rem 0.8rem;
            }}

            .app-header h1 {{
                margin: 0;
                font-size: 1.9rem;
                font-weight: 700;
                color: var(--header);
                letter-spacing: -0.02em;
            }}

            .app-header p {{
                margin: 0.35rem 0 0 0;
                color: var(--muted);
                font-size: 0.95rem;
                line-height: 1.5;
                max-width: 640px;
            }}

            /* Alerts */
            .stAlert, .stInfo, .stSuccess, .stWarning, .stError {{
                color: var(--fg) !important;
                border-radius: 10px !important;
                border-width: 1px !important;
            }}

            .stInfo {{
                background-color: var(--info-bg) !important;
                border-color: rgba(56, 189, 248, 0.3) !important;
            }}

            .stSuccess {{
                background-color: var(--success-bg) !important;
                border-color: rgba(34, 197, 94, 0.3) !important;
            }}

            .stWarning {{
                background-color: var(--warning-bg) !important;
                border-color: rgba(245, 158, 11, 0.3) !important;
            }}

            .stError {{
                background-color: var(--error-bg) !important;
                border-color: rgba(239, 68, 68, 0.3) !important;
            }}

            /* Buttons */
            .stButton button {{
                background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%) !important;
                color: white !important;
                border: none !important;
                border-radius: 10px !important;
                font-weight: 600 !important;
                padding: 0.6rem 1.1rem !important;
                transition: transform 0.15s ease, box-shadow 0.15s ease !important;
                box-shadow: 0 2px 8px rgba(20, 184, 166, 0.25) !important;
            }}

            .stButton button:hover {{
                transform: translateY(-1px);
                box-shadow: 0 6px 16px rgba(20, 184, 166, 0.35) !important;
            }}

            .stButton button:disabled {{
                opacity: 0.45 !important;
                box-shadow: none !important;
                transform: none !important;
            }}

            /* Text areas / file uploader */
            .stTextArea textarea, .stFileUploader {{
                border-radius: 10px !important;
                border: 1px solid var(--border) !important;
            }}

            .stMarkdown, .css-1d391kg {{
                color: var(--fg) !important;
            }}

            /* --- Upload page header --- */
            .section-header {{
                margin-bottom: 1.25rem;
            }}

            .section-header h2 {{
                margin: 0;
                font-size: 1.3rem;
                font-weight: 700;
                color: var(--header);
            }}

            .section-header p {{
                margin: 0.3rem 0 0 0;
                color: var(--muted);
                font-size: 0.92rem;
            }}

            /* --- Review report title --- */
            .report-title {{
                font-size: 1.5rem;
                font-weight: 700;
                color: var(--header);
                margin: 0.5rem 0 1.25rem 0;
            }}

            /* --- Summary stat card --- */
            .report-summary-card {{
                display: flex;
                flex-wrap: wrap;
                gap: 0.75rem;
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: 14px;
                padding: 1.1rem 1.25rem;
                margin-bottom: 1.5rem;
                box-shadow: var(--shadow);
            }}

            .summary-stat {{
                display: flex;
                flex-direction: column;
                gap: 0.2rem;
                min-width: 110px;
                padding: 0.4rem 1rem;
                border-right: 1px solid var(--border);
            }}

            .summary-stat:last-child {{
                border-right: none;
            }}

            .summary-stat-label {{
                font-size: 0.78rem;
                color: var(--muted);
                text-transform: uppercase;
                letter-spacing: 0.04em;
            }}

            .summary-stat-value {{
                font-size: 1.25rem;
                font-weight: 700;
                color: var(--header);
            }}

            /* --- Review category cards --- */
            .report-grid {{
                margin-bottom: 0.5rem;
            }}

            .review-card {{
                background: var(--card);
                border: 1px solid var(--border);
                border-left: 4px solid var(--muted);
                border-radius: 12px;
                padding: 1rem 1.2rem;
                margin-bottom: 1rem;
                box-shadow: var(--shadow);
            }}

            .review-card--warning {{ border-left-color: #f59e0b; }}
            .review-card--error   {{ border-left-color: #ef4444; }}
            .review-card--info    {{ border-left-color: #38bdf8; }}
            .review-card--success {{ border-left-color: #22c55e; }}

            .review-card-header {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 0.6rem;
            }}

            .review-card-icon {{
                font-size: 1.1rem;
            }}

            .review-card-title {{
                font-weight: 700;
                font-size: 0.98rem;
                color: var(--header);
                flex-grow: 1;
            }}

            .review-card-badge {{
                background: var(--surface);
                border: 1px solid var(--border);
                border-radius: 999px;
                padding: 0.1rem 0.6rem;
                font-size: 0.78rem;
                font-weight: 700;
                color: var(--muted);
            }}

            .review-list {{
                list-style: none;
                margin: 0;
                padding: 0;
            }}

            .review-item {{
                display: flex;
                align-items: flex-start;
                gap: 0.55rem;
                font-size: 0.88rem;
                color: var(--fg);
                padding: 0.35rem 0;
                border-top: 1px solid var(--border);
            }}

            .review-item:first-child {{
                border-top: none;
            }}

            .review-dot {{
                flex-shrink: 0;
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background: var(--muted);
                margin-top: 0.45rem;
            }}

            .review-empty {{
                font-size: 0.88rem;
                color: var(--muted);
                padding: 0.3rem 0;
            }}

            /* --- Explanation card --- */
            .explanation-card {{
                background: var(--accent-soft);
                border: 1px solid var(--border);
                border-radius: 12px;
                padding: 1.1rem 1.3rem;
                margin-top: 0.5rem;
            }}

            .explanation-header {{
                font-weight: 700;
                font-size: 1rem;
                color: var(--header);
                margin-bottom: 0.5rem;
            }}

            .explanation-body {{
                font-size: 0.9rem;
                color: var(--fg);
                line-height: 1.6;
                white-space: pre-wrap;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()