# Estrutura de dados para Clientes Físicos (Pessoa Física)

from Dados.pessoa import pessoa

class clienteFisico(pessoa):
    
    __cpf = None
    __dados = []
    
    def setCpf(self,cpf):

        self.__cpf=cpf

    def getCpf(self):

        return self.__cpf
    
    def setDados(self):

        nome = super().getNome()
        email = super().getEmail()
        endereco = super().getEndereco()
        telefone = super().getTelefone()
        
        dados=nome+"\t"+self.__cpf+"\t"+email+"\t"+endereco+"\t"+telefone

        self.__dados.append(dados)

    def getDados(self):

        return self.__dados