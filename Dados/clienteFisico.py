# Estrutura de dados para Clientes Físicos (Pessoa Física)

from Dados.pessoa import Pessoa

class clienteFisico(Pessoa):
    
    __cpf = None
    __dados = []
    
    def setCpf(self,cpf):

        __cpf=cpf

    def getCpf(self):

        return __cpf
    
    def setDados(self,dados):

        __dados=dados

    def getDados(self):

        return __dados