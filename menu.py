# Este arquivo será executado para fazer operações nos dados

# Importar as classes usadas no código

import time,os
from Dados.clienteFisico import clienteFisico
from Dados.clienteJuridico import clienteJuridico

# Criar objetos das classes que serão utilizadas

clienteJuridico=clienteJuridico()
clienteFisico=clienteFisico()

# Função que faz o menu do programa

def programa():

    while True:
        
        # Pergunta de qual ação o usuário deseja fazer
         
        acao = input("Qual ação deseja efetuar? \n\n 1 - Cadastrar novo cliente \n 2 - Excluir cliente \n 3 - Editar cliente \n 5 - Listar clientes \n 9 - Finalizar Programa\n\n Resposta: ")

        if (acao=="9"):
            return "S"

        # Chama função para definir a descricão a apresentar na seleção de classificação do cliente

        descricaoAcao=definirDescricao(acao)
        if (descricaoAcao==0):
            return "N"

        # Seleção de classificação do Cliente

        classificacao = input("\n\n"+descricaoAcao+" cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n Resposta: ")
        print("\n")

        # Match da ação seguir caminho de operação informado pelo usuário

        match(acao):
            
            case "1":
                
                nomeCliente = input("Nome do cliente: ")
                enderecoCliente = input("Endereço do cliente: ")
                emailCliente = input("Email do cliente: ")
                telefoneCliente = input("Telefone do cliente: ")

                if (classificacao=="1"):
                    
                    cnpjCliente = input("CNPJ do cliente: ")

                    clienteJuridico.setCnpj(cnpjCliente)
                    clienteJuridico.setEmail(emailCliente)
                    clienteJuridico.setEndereco(enderecoCliente)
                    clienteJuridico.setNome(nomeCliente)
                    clienteJuridico.setTelefone(telefoneCliente)

                    clienteJuridico.setDados()
                
                if (classificacao=="2"):
                    
                    cpfCliente = input("CPF do cliente: ")
                    
                    clienteFisico.setCpf(cpfCliente)
                    clienteFisico.setEmail(emailCliente)
                    clienteFisico.setEndereco(enderecoCliente)
                    clienteFisico.setNome(nomeCliente)
                    clienteFisico.setTelefone(telefoneCliente)
                    
                    clienteFisico.setDados()
        
                os.system("cls")
                    
            case "2":
                
                print(acao)
        
                os.system("cls")
                
            case "3":
                
                print(acao)
        
                os.system("cls")

            case "5":

                statusCode=imprimirDados(classificacao)
                
                if (statusCode==0):
                    return "N"

# Função para imprimir clientes em tela da classificação informada

def imprimirDados(classificacao):
    
    listaClientes = None
    
    if (classificacao=="1"):

        listaClientes=clienteJuridico.getDados()

    if (classificacao=="2"):
                
        listaClientes=clienteFisico.getDados()
            
    if (listaClientes==None):
        print("\nNenhum cadastro encontrado!\n")
        time.sleep(3)
        return 0

    for identificador,cliente in enumerate(listaClientes):
            
        print(identificador," - ",cliente)

    print("\n")

    return 1

# Match para definir a descrição da ação a apresentar na definição da classificação do cliente

def definirDescricao(acao):

    match(acao):
            
        case "1":
                
            descricaoAcao="Cadastrar"

            return descricaoAcao
                
        case "2":
                
            descricaoAcao="Excluir"

            return descricaoAcao
                
        case "3":
                
            descricaoAcao="Editar"
                
            return descricaoAcao

        case "5":
            
            descricaoAcao="Listar"

            return descricaoAcao

        case _:
                
            print("\nAção Inválida!\n")
            time.sleep(3)
            return 0

# Executa o programa e faz o controle da saída

pergunta=1

while True:
    sair=programa()
    if (sair=="S"):
        break