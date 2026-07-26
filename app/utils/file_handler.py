import os
from pathlib import Path


class FileHandler:
    """
    Handles reading and writing files.
    """

    @staticmethod
    def read_file(file_path):
        """
        Read a text file.
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found.")

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def save_file(file_path, content):
        """
        Save content to a file.
        """
        path = Path(file_path)

        os.makedirs(path.parent, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def get_extension(filename):
        return Path(filename).suffix

    @staticmethod
    def get_filename(filename):
        return Path(filename).stem

    @staticmethod
    def exists(file_path):
        return Path(file_path).exists()