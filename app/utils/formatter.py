import json


class Formatter:

    @staticmethod
    def markdown(title, content):

        return f"# {title}\n\n{content}"

    @staticmethod
    def json(data):

        return json.dumps(data, indent=4)

    @staticmethod
    def bullet(items):

        return "\n".join([f"- {i}" for i in items])

    @staticmethod
    def separator():

        return "\n" + "-" * 60 + "\n"

    @staticmethod
    def code_block(code, language="python"):

        return f"```{language}\n{code}\n```"