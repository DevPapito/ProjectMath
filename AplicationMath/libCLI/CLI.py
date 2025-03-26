import os

class ToolsCLI():
    
    @classmethod
    def bord_Of_Message(cls,chars:int) -> str:

        bordString = ""

        for i in range((chars)):
            bordString += "-"

        return bordString

    @classmethod
    def tratament_Input(cls,string_tratament:str) -> str:
        tratament_local = ""

        tratament_local = string_tratament.lower()

        return tratament_local


class CLI():

    # message ------

    @classmethod
    def start_Message(cls) -> None:
        os.system("echo Programa inicializado")

    @classmethod
    def message_Error(cls,message_Error:str) -> None:
        cls.color_Terminal(4)
        cls.generic_Message(message_Error)
    
    @classmethod
    def generic_Message(cls,message:str) -> None:
        message_size = len(message)

        print(ToolsCLI.bord_Of_Message(message_size))
        os.system(f"echo {message}")
        print(ToolsCLI.bord_Of_Message(message_size))
    
    @classmethod
    def dev_Tool_Message(cls,message:str) -> None:

        cls.color_Terminal(6)
        print(f">>>>>>>>>>>  {message}  <<<<<<<<<<<<<")
    
    @classmethod
    def view_Dev_Tool_Message(cls,message:str) -> None:
        
        cls.dev_Tool_Message(f"Tipo do string: {type(message)}")                
        cls.dev_Tool_Message(f"Representacao do valor: {message}")

    # Terminal ------

    @classmethod
    def clear_Terminal(cls) -> None:
        os.system("cls")

    @classmethod
    def color_Terminal(cls,color:int) -> None:

        if (color > 9):
            os.system('color 0F')
            raise RuntimeError('Cor nao identificada alterando para padrao')
        
        os.system(f'color 0{color}')
    
    # Inputs Terminal -----

    @classmethod
    def generic_Input(cls,type:str,message_input:str,devTool:bool) -> object:

        type_input = ToolsCLI.tratament_Input(type)

        # testar float
        if ('float' in type_input):
            
            getLocal = float(input(message_input))  

            if (devTool):
                
                cls.view_Dev_Tool_Message(getLocal)

            return getLocal
            
        elif ('int' in type_input):

            getLocal = int(input(message_input))

            if (devTool):

                cls.view_Dev_Tool_Message(getLocal)

            return getLocal

        elif ('bool' in type_input):

            getLocal = bool(input(message_input))

            if (devTool):

                cls.view_Dev_Tool_Message(getLocal)

            return getLocal
            
        elif ('str' in type_input):
            getLocal = input(message_input)

            if (devTool):

                cls.view_Dev_Tool_Message(getLocal)
            
            return getLocal
        
        else:
            cls.message_Error('Tipo nao valido para o metodo')




