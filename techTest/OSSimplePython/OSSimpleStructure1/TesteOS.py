from os import system

class TesteOS():
    def __init__(self):
        pass
    
    def testeLocal(self):
        # Esse formato a limitacoes como a necessidade obrigatoria de um terminal aberto que seja de PROMP CMD 
        # E uso de execo a comando duplicados ou unificados CMD/DOS
        
        system('cd E:\\ProjectAplicationMath\\techTest\\OSSimplePython\\OSSimpleStructure1\\imagens\\ & echo Ola mundo :D > Pinto.txt')

if __name__ == '__main__':
    testeOS = TesteOS()
    testeOS.testeLocal()

