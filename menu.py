# Este arquivo será executado para fazer operações nos dados

# Importar as classes usadas no código

import time,os
from Dados.clienteFisico import clienteFisico
from Dados.clienteJuridico import clienteJuridico

# Criação da lista onde ficarão armazenados os objetos de clientes

clientes = []

# Função que faz o menu do programa

def programa():

    while True:
        
        # Pergunta de qual ação o usuário deseja fazer
         
        acao = input("Qual ação deseja efetuar? \n\n 1 - Cadastrar novo cliente \n 2 - Excluir cliente \n 3 - Editar cliente \n 4 - Listar clientes \n\n 9 - Finalizar Programa\n\n Resposta: ")

        if (acao=="9"):
            return "S"

        # Chama função para definir a descricão a apresentar na seleção de classificação do cliente

        descricaoAcao=definirDescricao(acao)
        if (descricaoAcao==0):
            os.system("cls")
            return "N"
        
        os.system("cls")
        
        print("Ação: ",descricaoAcao.split(":")[0],"\n\n")
        
        # Seleção de classificação do Cliente

        classificacao = input(descricaoAcao)
        print("\n")
        
        if classificacao=="9":
            os.system("cls")
            return "N"

        if (acao!="4")&(classificacao=="3"):
            print("\nClassificação Inválida!\n")
            time.sleep(3)
            os.system("cls")
            return "N"

        descricaoClassificacao=obterDescricaoClassificacao(classificacao)
        if descricaoClassificacao=="N":
            os.system("cls")
            return "N"
        
        os.system("cls")
        
        print("Ação: ",descricaoAcao.split(":")[0])
        print("Classificação: ",descricaoClassificacao,"\n")
        
        # Match da ação seguir caminho de operação informado pelo usuário

        match(acao):
            
            # Caso a ação for igual a 1 segue o caminho para cadastrar um novo cliente
            
            case "1":
                
                codigoIdentificador = input("Código de identificação: ")
                statusCode=validarCodigoIdentificador(codigoIdentificador)
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

                    clientes.append(clienteJuridico(nomeCliente,enderecoCliente,emailCliente,telefoneCliente,cnpjCliente,codigoIdentificador,classificacao))

                if (classificacao=="2"):
                    
                    cpfCliente = input("CPF do cliente: ")
                    
                    clientes.append(clienteFisico(nomeCliente,enderecoCliente,emailCliente,telefoneCliente,cpfCliente,codigoIdentificador,classificacao))
        
                os.system("cls")
                return "N"
                    
            case "2":
                
                print(acao)
        
                os.system("cls")
                
            case "3":
                
                print(acao)
        
                os.system("cls")

            # Caso a ação for igual a 4 segue o caminho para listar os clientes
            
            case "4":

                statusCode=imprimirDados(classificacao)
                
                if (statusCode==0):
                    return "N"
                
                input("\n\n Sair(Enter)")
                os.system("cls")
                return "N"

# Função para imprimir clientes em tela da classificação informada

def imprimirDados(classificacaoSelecionada):
    
    print("-"*179)
    
    if classificacaoSelecionada=="1":
        print('| {0:20} | {1:20} | {2:30} | {3:30} | {4:20} | {5:40} |'.format("ID","CNPJ","Nome","E-Mail","Telefone","Endereço"))
    if classificacaoSelecionada=="2":
        print('| {0:20} | {1:20} | {2:30} | {3:30} | {4:20} | {5:40} |'.format("ID","CPF","Nome","E-Mail","Telefone","Endereço"))
    if classificacaoSelecionada=="3":
        print('| {0:20} | {1:20} | {2:30} | {3:30} | {4:20} | {5:40} |'.format("ID","CNPJ/CPF","Nome","E-Mail","Telefone","Endereço"))
    
    print("-"*179)
  
    for indice,cliente in enumerate(clientes):

        classificacao = cliente.getClassificacao()
            
        if (classificacao=="1")&(classificacaoSelecionada=="3" or classificacaoSelecionada=="1"):
                
            print('| {0:20} | {1:20} | {2:30} | {3:30} | {4:20} | {5:40} |'.format(str(cliente.getIdentificador()),str(cliente.getCnpj()),str(cliente.getNome()),str(cliente.getEmail()),str(cliente.getTelefone()),str(cliente.getEndereco())))
            
        if (classificacao=="2")&(classificacaoSelecionada=="3" or classificacaoSelecionada=="2"):
                
            print('| {0:20} | {1:20} | {2:30} | {3:30} | {4:20} | {5:40} |'.format(str(cliente.getIdentificador()),str(cliente.getCpf()),str(cliente.getNome()),str(cliente.getEmail()),str(cliente.getTelefone()),str(cliente.getEndereco())))
    
    print("-"*179)
    
    return 1
    
# Match para definir a descrição da ação a apresentar na definição da classificação do cliente

def definirDescricao(acao):

    match(acao):
            
        case "1":
                
            descricaoAcao="Cadastrar cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n 9 - Voltar \n\n Resposta: "

            return descricaoAcao
                
        case "2":
                
            descricaoAcao="Excluir cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n 9 - Voltar \n\n Resposta: "

            return descricaoAcao
                
        case "3":
                
            descricaoAcao="Editar cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n 9 - Voltar \n\n Resposta: "
                
            return descricaoAcao

        case "4":
            
            descricaoAcao="Listar cliente: \n\n 1 - Jurídico \n 2 - Físico \n 3 - Todos \n\n 9 - Voltar \n\n Resposta: "

            return descricaoAcao

        case _:
                
            print("\nAção Inválida!\n")
            time.sleep(3)
            return 0

# Validação executada ao usuário informar identificador, deve ser único !!!

def validarCodigoIdentificador(codigoIdentificador):
        
    for indice,cliente in enumerate(clientes):

        if codigoIdentificador==cliente.getIdentificador():
            return 0
        
    return 1

# Função para obter a descrição da classificação selecionada

def obterDescricaoClassificacao(classificacao):
    
    match(classificacao):
        
        case "1":
            
            return "Pessoa Jurídica"
        
        case "2":
            
            return "Pessoa Física"
        
        case "3":
            
            return "Todos"
        
        case _:
            
            print("\nClassificação Inválida!\n")
            time.sleep(3)
            return "N"

# Executa o programa e faz o controle da saída

while True:
    sair=programa()
    if (sair=="S"):
        break