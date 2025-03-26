from os import system

class MakeColorTerm():
    def __init__ (self,numberInteger:int):
        self.integer = numberInteger
    
    def makeTerminalColor(self):
        system(f'color {self.integer}')
