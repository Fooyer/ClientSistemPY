# Estrutura de dados para Clientes Jurídicos (Pessoa Jurídica)

from Dados.pessoa import pessoa

class clienteJuridico(pessoa):
    
    __cnpj = None
    __dados = []
    __proximoId = 0
    
    def setCnpj(self,cnpj):

        self.__cnpj=cnpj

    def getCnpj(self):

        return self.__cnpj
    
    def setDados(self):
        
        nome = super().getNome()
        email = super().getEmail()
        endereco = super().getEndereco()
        telefone = super().getTelefone()

        dados=nome+"^"+self.__cnpj+"^"+email+"^"+endereco+"^"+telefone

        self.__dados.append(dados)

        self.__proximoId=self.__proximoId + 1

    def getDados(self):

        return self.__dados