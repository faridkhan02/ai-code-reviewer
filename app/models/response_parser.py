"""
Response Parser
"""

import re


class ResponseParser:

    def __init__(self):

        pass

    def parse(self, response):

        sections = {

            "summary": "",

            "bugs": "",

            "security": "",

            "performance": "",

            "quality": "",

            "best_practices": "",

            "score": "",

            "improved_code": ""

        }

        patterns = {

            "summary": r"## Summary(.*?)(?=##|$)",

            "bugs": r"## Bugs(.*?)(?=##|$)",

            "security": r"## Security Issues(.*?)(?=##|$)",

            "performance": r"## Performance Improvements(.*?)(?=##|$)",

            "quality": r"## Code Quality(.*?)(?=##|$)",

            "best_practices": r"## Best Practices(.*?)(?=##|$)",

            "score": r"## Final Score.*?(.*?)(?=##|$)",

            "improved_code": r"## Improved Version.*?(.*?)(?=##|$)"

        }

        for key, pattern in patterns.items():

            match = re.search(

                pattern,

                response,

                re.DOTALL | re.IGNORECASE

            )

            if match:

                sections[key] = match.group(1).strip()

        return sections