# Classe main de pessoa, todas as outras classes que tem relação com pessoa deverão herdar dessa


class pessoa:

    __nome = None
    __endereco = None
    __email = None
    __telefone = None
    __identificador = None
    
    def setIdentificador(self,identificador):

        self.__identificador=identificador

    def getIdentificador(self):

        return self.__identificador
    
    def setNome(self,nome):

        self.__nome = nome

    def getNome(self):

        return self.__nome
          
    def setEndereco(self,endereco):

        self.__endereco = endereco

    def getEndereco(self):

        return self.__endereco
          
    def setEmail(self,email):

        self.__email = email

    def getEmail(self):

        return self.__email
          
    def setTelefone(self,telefone):

        self.__telefone = telefone

    def getTelefone(self):

        return self.__telefone