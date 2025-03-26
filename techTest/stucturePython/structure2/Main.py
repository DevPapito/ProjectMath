from lib import MakeColorTerm, ForceError

class Main():
    
    def __init__(self,runtime:bool):
        self.runtime = runtime
        self.makeColor = MakeColorTerm(3)

    def main(self):

        forceError = ForceError()

        self.makeColor.makeTerminalColor()
        forceError.force1()

if __name__ == '__main__':
    mainObj = Main(True)
    mainObj.main()