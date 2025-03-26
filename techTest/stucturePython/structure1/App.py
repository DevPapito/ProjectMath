from codesForInput import Inputs

input = Inputs()

class App():
    
    input = Inputs()

    @classmethod
    def main(cls):

        try:
            cls.input.printHi()
            cls.input.printBye()

            cls.input.setFloatPrivado(float(input("Digite um float")))

            print(cls.input.getFloatPrivado)

            raise RuntimeError('Programa iniciado')
        except (RuntimeError):
            pass

if __name__ == '__main__':
    App().main()