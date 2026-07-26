"""
Utility Functions
"""

import streamlit as st
import os


def load_css(css_file: str):
    """
    Load a CSS file into the Streamlit app.

    Args:
        css_file (str): Path to the CSS file.
    """

    if os.path.exists(css_file):
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )
    else:
        st.warning(f"CSS file not found: {css_file}") 