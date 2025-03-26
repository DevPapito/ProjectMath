import os

class TesteOS():
    def __init__(self):
        
        self.__PATH_IMAGES = r"E:\ProjectAplicationMath\techTest\OSSimplePython\OSSimpleStructure2\imagens"
        self.__path_complet_variable = ""

    def make_Directory(self,name_dir:str):

        # opcional pois o proprio Win ja permite a verificacao
        # if (name_dir in os.path.join(self.__PATH_IMAGES,name_dir)):
        #     raise RuntimeError(f"Ja existe um diretorio com o nome: {name_dir}")
        
        self.__path_complet_variable = os.path.join(self.__PATH_IMAGES,name_dir)
        os.system(f"cd {self.__PATH_IMAGES} & mkdir {name_dir}")
    
    def overwrite_In_Directory(self,old_name_dir:str,new_name_dir:str):
        
        # erro logico possivel
        # em que a ultima atualizacao de make_Directory caso nao seja percebivel
        # pode-se a lervar erro logico em que nunca sera atualizado o diretorio
        # pois o elemento a seguir nao verifica o geral de x elementos logicos
        # mas somente de um especificado

        if (not (old_name_dir in self.__path_complet_variable)):
            raise RuntimeError(f'Diretorio nao encontrado ou nao existe em {self.__path_complet_variable}')
        
        os.system(f"cd {self.__path_complet_variable} & ren {old_name_dir} {new_name_dir}")
    
    def make_FileAndType(self,name_file:str,type_file:str,name_dir_pointer:str):
        
        if (not (name_dir_pointer in self.__path_complet_variable)):
            raise RuntimeError('Diretorio apontado nao existe no sistema')
        
        print("Foi criado o seguinte caminho",self.__path_complet_variable)
        os.system(f"cd {self.__path_complet_variable} & echo > {name_file}.{type_file}")


if __name__ == '__main__':
    tsOS = TesteOS()
    tsOS.make_Directory("CodigosJava")
    tsOS.make_FileAndType(name_file="Javinha",type_file="java",name_dir_pointer="CodigosJava")
    tsOS.overwrite_In_Directory("CodigosJava", "CodigosJavaESptringBoot")