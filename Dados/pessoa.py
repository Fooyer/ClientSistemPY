# Classe main de pessoa, todas as outras classes que tem relação com pessoa deverão herdar dessa


class Pessoa:

    __nome = None
    __endereco = None
    __email = None
    __telefone = None
    
    def setNome(self,nome):

        __nome=nome

    def getNome(self):

        return __nome
          
    def setEndereco(self,endereco):

        __endereco=endereco

    def getEndereco(self):

        return __endereco
          
    def setEmail(self,email):

        __email=email

    def getEmail(self):

        return __email
          
    def setTelefone(self,telefone):

        __telefone=telefone

    def getTelefone(self):

        return __telefone