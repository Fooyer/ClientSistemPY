# Estrutura de dados para Clientes Jurídicos (Pessoa Jurídica)

from Dados.pessoa import pessoa

class clienteJuridico(pessoa):
    
    __cnpj = None
    __dados = []
    
    def setCnpj(self,cnpj):

        self.__cnpj=cnpj

    def getCnpj(self):

        return self.__cnpj
    
    def setDados(self):
        
        nome = super().getNome()
        email = super().getEmail()
        endereco = super().getEndereco()
        telefone = super().getTelefone()

        dados=nome+"\t"+self.__cnpj+"\t"+email+"\t"+endereco+"\t"+telefone

        self.__dados.append(dados)

    def getDados(self):

        return self.__dados