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
        
        # Seleção de classificação do Cliente em caso de cadastro e listagem

        if acao=="1" or acao=="4":
            
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
                
                print("\nPara cancelar dê enter com um valor nulo.\n")
                
                codigoIdentificador = input("Código de identificação: ")
                if codigoIdentificador=="":
                    os.system("cls")
                    return "N"
                statusCode=validarCodigoIdentificador(codigoIdentificador)
                if statusCode==0:
                    print("\nCódigo de Identificador Já Utilizado!\n")
                    time.sleep(4)
                    os.system("cls")
                    return "N"

                nomeCliente = input("Nome do cliente: ")
                if nomeCliente=="":
                    os.system("cls")
                    return "N"
                
                enderecoCliente = input("Endereço do cliente: ")
                if enderecoCliente=="":
                    os.system("cls")
                    return "N"
                
                emailCliente = input("Email do cliente: ")
                if emailCliente=="":
                    os.system("cls")
                    return "N"
                
                telefoneCliente = input("Telefone do cliente: ")
                if telefoneCliente=="":
                    os.system("cls")
                    return "N"

                if (classificacao=="1"):
                    
                    cnpjCliente = input("CNPJ do cliente: ")
                    if cnpjCliente=="":
                        os.system("cls")
                        return "N"
                    
                    clientes.append(clienteJuridico(nomeCliente,enderecoCliente,emailCliente,telefoneCliente,cnpjCliente,codigoIdentificador,classificacao))

                if (classificacao=="2"):
                    
                    cpfCliente = input("CPF do cliente: ")
                    if cpfCliente=="":
                        os.system("cls")
                        return "N"
                    
                    clientes.append(clienteFisico(nomeCliente,enderecoCliente,emailCliente,telefoneCliente,cpfCliente,codigoIdentificador,classificacao))
        
                os.system("cls")
                return "N"
                    
            # Caso a ação for igual a 2 segue o caminho para Excluir um cliente pelo seu ID    
                
            case "2":
                
                identificador = input("Identificador do cliente: ")
                print("\n")
                
                flagAlteracao=0
                
                for index,cliente in enumerate(clientes):
                    
                    if cliente.getIdentificador()==identificador:
                        
                        confirmacao = input("Tem certeza que deseja deletar o cliente "+str(cliente.getNome())+" do cadastro?\n\n 1 - Sim \n 2 - Não \n\n Resposta: ")
                        
                        if (confirmacao!="1")&(confirmacao!="2"):
                            print("\nOpção inválida!")
                            time.sleep(3)
                            os.system("cls")
                        
                        if confirmacao=="1":
                            del clientes[index]
                            flagAlteracao=1
                        else:
                            os.system("cls")
                            return "N"
                
                if flagAlteracao==1:
                    
                    print("\nCliente excluído com sucesso.")
                    time.sleep(3)
                    os.system("cls")
                    
                else:
                    print("\nCliente não encontrado.")
                    time.sleep(3)
                    os.system("cls")
                    
            # Caso a ação for igual a 3 segue o caminho para Editar um cliente existente
                
            case "3":
                
                identificador = input("Identificador do cliente: ")
                print("\n")
        
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
                
            descricaoAcao="Cadastrar Cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n 9 - Voltar \n\n Resposta: "

            return descricaoAcao
                
        case "2":
                
            descricaoAcao="Excluir Cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n 9 - Voltar \n\n Resposta: "

            return descricaoAcao
                
        case "3":
                
            descricaoAcao="Editar Cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n 9 - Voltar \n\n Resposta: "
                
            return descricaoAcao

        case "4":
            
            descricaoAcao="Listar Clientes: \n\n 1 - Jurídico \n 2 - Físico \n 3 - Todos \n\n 9 - Voltar \n\n Resposta: "

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