# Estrutura de dados para Clientes Físicos (Pessoa Física)

from Dados.pessoa import pessoa

class clienteFisico(pessoa):
    
    __cpf = None
    __dados = []
    
    def setCpf(self,cpf):

        self.__cpf=cpf

    def getCpf(self):

        return self.__cpf
    
    def setDados(self,dados):

        self.__dados=dados

    def getDados(self):

        return self.__dados