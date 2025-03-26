from webservice import WebService

class App():
    def __init__(self):
        self.__webservice = WebService()
        self.__HTTP_PATH_GOOLE = "http://google.com"
        self.__HTTP_PATH_FACEBOOK = "http://facebook.com"

    def run(self):
        print('Executando!')
        self.__webservice.viewWeb(self.__HTTP_PATH_GOOLE)
        self.__webservice.viewWeb(self.__HTTP_PATH_FACEBOOK)

    def start(self):
        self.run()

if __name__ == '__main__':
    app = App()
    app.start()