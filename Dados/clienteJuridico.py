# Estrutura de dados para Clientes Jurídicos (Pessoa Jurídica)

from Dados.pessoa import Pessoa

class clienteJuridico(Pessoa):
    
    __cnpj = None
    __inscricaoEstadual = None
    __dados = []
    
    def setCnpj(self,cnpj):

        __cnpj=cnpj

    def getCnpj(self):

        return __cnpj

    def setInscricaoEstadual(self,inscricaoEstadual):

        __inscricaoEstadual=inscricaoEstadual

    def getInscricaoEstadual(self):

        return __inscricaoEstadual
    
    def setDados(self,dados):

        __dados=dados

    def getDados(self):

        return __dados