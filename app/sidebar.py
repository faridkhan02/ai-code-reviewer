"""
Sidebar Components
"""

import streamlit as st


def render_sidebar():
    """
    Render the sidebar and return user settings.
    """

    st.sidebar.title("⚙️ AI Review Settings")

    settings = {
        "bug_detection": st.sidebar.checkbox(
            "Bug Detection",
            value=True,
        ),
        "security_analysis": st.sidebar.checkbox(
            "Security Analysis",
            value=True,
        ),
        "performance_analysis": st.sidebar.checkbox(
            "Performance Analysis",
            value=True,
        ),
        "style_analysis": st.sidebar.checkbox(
            "Code Style",
            value=True,
        ),
        "ai_explanation": st.sidebar.checkbox(
            "AI Explanation",
            value=True,
        ),
        "theme": st.sidebar.selectbox(
            "Theme",
            ["Light", "Dark"],
            index=1,
            help="Choose light or dark mode for the app UI.",
        ),
    }

    st.sidebar.markdown("---")

    st.sidebar.info("AI Code Reviewer v1.0")

    return settings 