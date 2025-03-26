from libGeneric import AutoCLI

class App():
    def __init__(self):
        self.__autoCli = AutoCLI()

    def run(self):
        print("Executando")
        self.__autoCli.viewDirector()
        self.__autoCli.blueTerminal()

    def start(self):
        self.run()

if __name__ == '__main__':
    app = App()
    app.start()
