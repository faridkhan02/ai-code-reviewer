import subprocess
import sys
from pathlib import Path


def run_streamlit():
    """
    Launch the Streamlit application.
    """

    app_path = Path("app/main.py")

    if not app_path.exists():
        print("Error: app/main.py not found.")
        sys.exit(1)

    subprocess.run(
        [
            "streamlit",
            "run",
            str(app_path),
        ]
    )


if __name__ == "__main__":
    run_streamlit()