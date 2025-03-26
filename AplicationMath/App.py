from libCLI import CLI

from time import sleep

class App():

    run_Time = False;

    @classmethod
    def run(cls):
        # variaveis locais de ambiente
        contador = 1

        # espaco programavel
        # possivel tratamento dentro de um try e while encadeado para futuro

        while (cls.run_Time != False):
            sleep(0.3)
            CLI.color_Terminal(3)
            CLI.generic_Message("Ola mundo! :D")
            CLI.start_Message()
            print(f"Giro: {contador}")

            if (contador == 2):
                print(type(CLI.generic_Input('bool',"Digite um numero: ",True)))
                raise RuntimeError('O programa comecou')
            
            contador += 1

            CLI.clear_Terminal()

    @classmethod
    def start(cls):
        # inicializadores 

        cls.run_Time = True
        cls.run()


if __name__ == '__main__':
    App().start()