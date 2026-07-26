import time
import uuid
from datetime import datetime


class Helpers:

    @staticmethod
    def generate_report_name():

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        return f"report_{timestamp}.md"

    @staticmethod
    def generate_unique_id():

        return str(uuid.uuid4())

    @staticmethod
    def current_time():

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def execution_time(start_time):

        return round(time.time() - start_time, 3)

    @staticmethod
    def truncate(text, length=200):

        if len(text) <= length:
            return text

        return text[:length] + "..."

    @staticmethod
    def count_lines(code):

        return len(code.splitlines())

    @staticmethod
    def count_words(text):

        return len(text.split())