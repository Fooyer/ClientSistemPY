# Estrutura de dados para Clientes Jurídicos (Pessoa Jurídica)

from Dados.pessoa import pessoa

class clienteJuridico(pessoa):
    
    __cnpj = None
    
    def __init__(self,nomeCliente,enderecoCliente,emailCliente,telefoneCliente,cnpjCliente,identificador,classificacao):
        
        self.setCnpj(cnpjCliente)
        self.setEmail(emailCliente)
        self.setEndereco(enderecoCliente)
        self.setNome(nomeCliente)
        self.setTelefone(telefoneCliente)
        self.setIdentificador(identificador)
        self.setClassificacao(classificacao)

    def setCnpj(self,cnpj):

        self.__cnpj=cnpj

    def getCnpj(self):

        return self.__cnpj