# Estrutura de dados para Clientes Físicos (Pessoa Física)

from Dados.pessoa import pessoa

class clienteFisico(pessoa):
    
    __cpf = None

    def __init__(self,nomeCliente,enderecoCliente,emailCliente,telefoneCliente,cpfCliente,identificador,classificacao):
        
        self.setCpf(cpfCliente)
        self.setEmail(emailCliente)
        self.setEndereco(enderecoCliente)
        self.setNome(nomeCliente)
        self.setTelefone(telefoneCliente)
        self.setIdentificador(identificador)
        self.setClassificacao(classificacao)
    
    def setCpf(self,cpf):

        self.__cpf=cpf

    def getCpf(self):

        return self.__cpf