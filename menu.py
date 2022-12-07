# Este arquivo será executado para fazer operações nos dados

# Importar as classes usadas no código

import time,os
from Dados.clienteFisico import clienteFisico
from Dados.clienteJuridico import clienteJuridico

clientes = []

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
                
                codigoIdentificador = input("Código de identificação: ")
                statusCode=validarCodigoIdentificador(classificacao,codigoIdentificador)
                if statusCode==0:
                    print("\nCódigo de Identificador Já Utilizado!\n")
                    time.sleep(3)
                    return "N"

                nomeCliente = input("Nome do cliente: ")
                enderecoCliente = input("Endereço do cliente: ")
                emailCliente = input("Email do cliente: ")
                telefoneCliente = input("Telefone do cliente: ")

                if (classificacao=="1"):
                    
                    cnpjCliente = input("CNPJ do cliente: ")

                    clientes.append(clienteJuridico(nomeCliente,enderecoCliente,emailCliente,telefoneCliente,cnpjCliente,codigoIdentificador))

                if (classificacao=="2"):
                    
                    cpfCliente = input("CPF do cliente: ")
                    
                    clientes.append(clienteFisico(nomeCliente,enderecoCliente,emailCliente,telefoneCliente,cpfCliente,codigoIdentificador))
        
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
       
    print('{0:20} | {1:20} | {2:30} | {3:30} | {4:20} | {5:40}'.format("ID","CNPJ","Nome","E-Mail","Telefone","Endereço"))
    print("-"*150)

    for indice,cliente in enumerate(clientes):

        if cliente.getCnpj():
            
            print('{0:20} | {1:20} | {2:30} | {3:30} | {4:20} | {5:40}'.format(str(cliente.getIdentificador()),str(cliente.getCnpj()),str(cliente.getNome()),str(cliente.getEmail()),str(cliente.getTelefone()),str(cliente.getEndereco())))
        
        elif cliente.getCpf():
            
            print('{0:20} | {1:20} | {2:30} | {3:30} | {4:20} | {5:40}'.format(str(cliente.getIdentificador()),str(cliente.getCpf()),str(cliente.getNome()),str(cliente.getEmail()),str(cliente.getTelefone()),str(cliente.getEndereco())))

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

def validarCodigoIdentificador(classificacao,codigoIdentificador):
        
    for indice,cliente in enumerate(clientes):

        if codigoIdentificador==cliente.getIdentificador():
            return 0
        
    return 1

# Executa o programa e faz o controle da saída

while True:
    sair=programa()
    if (sair=="S"):
        break