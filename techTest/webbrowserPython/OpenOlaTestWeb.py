import webbrowser

class OpenOlaTesteWeb():
    def __init__(self):
        pass

    def openOla(self) -> None:

        webbrowser.open("google.com")
        webbrowser.open("youtube.com",new=2,autoraise=True)
        webbrowser.open_new_tab("google.com")
        webbrowser.open_new("google.com")
        webbrowser.open("E:\\ProjectAplicationMath\\techTest\\webbrowserPython\\codesHtml\\OlaTeste.html")
        webbrowser.open("E:\\ProjectAplicationMath\\techTest\\webbrowserPython\\codesHtml\\TchauTeste.html")

if __name__ == '__main__':
    opw = OpenOlaTesteWeb()

    opw.openOla()

