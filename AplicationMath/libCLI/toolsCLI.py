class ToolsCLI():
    def __init__(self):
        pass

    def bord_of_message(chars:int) -> str:

        bordString = ""

        for i in range((chars)):
            bordString += "-"

        return bordString


