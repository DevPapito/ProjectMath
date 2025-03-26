class Inputs():
    def __init__(self):
                
        self.inteiro = 0
        self.__floatPrivado = 0.0

    def printHi(self) -> None:
        print('Hi!')
    
    def printBye(self) -> None:
        print('Bye')
    
    # setter

    def setFloatPrivado(self,numeroFloat:float) -> None:

        self.__floatPrivado = numeroFloat
    
    # getter

    def getFloatPrivado(self) -> float:

        return self.__floatPrivado

    
