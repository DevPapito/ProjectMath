class AppTeste1():
    def __init__(self):
        pass

    def setApp(self) -> bool:

        entry = input("Digite y ou n: ")
        entry = entry.lower()

        if (not 'y' in entry):
            
            return False
        
        return True
    
    def start(self,boolean:bool) -> None:

        while (boolean):
            print('Process')
        
        print('Encerrer process')

if __name__ == '__main__':
    appt1 = AppTeste1()
    appt1.start(appt1.setApp())
