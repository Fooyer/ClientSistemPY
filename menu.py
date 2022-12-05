# Este arquivo será executado para fazer operações nos dados

# Importar as classes usadas no código

import time
from Dados.clienteFisico import clienteFisico
from Dados.clienteJuridico import clienteJuridico

# Criar objetos das classes que serão utilizadas

clienteJuridico=clienteJuridico()
clienteFisico=clienteFisico()

# Pergunta de qual ação o usuário deseja fazer

acao = input("Qual ação deseja efetuar? \n\n 1 - Cadastrar novo cliente \n 2 - Excluir cliente \n 3 - Editar cliente \n\n Resposta: ")

# Match para definir a descrição da ação a apresentar na definição da classificação do cliente

match(acao):
    
    case "1":
        
        descricaoAcao="Cadastrar"
        
    case "2":
        
        descricaoAcao="Excluir"
        
    case "3":
        
        descricaoAcao="Editar"
        
    case _:
        
        print("\nAção Inválida!\n")
        descricaoAcao = None
        time.sleep(3)
        exit()

# Seleção de classificação do Cliente

classificacao = input("\n\n"+descricaoAcao+" cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n Resposta: ")

# Gera os dados da classificação escolhida pelo cliente

if (classificacao=="1"):

    listaClientes=clienteJuridico.getDados()

# Apresenta a lista de clientes com a classificação no sistema se a opção não for de cadastro


if (acao!=1):
    for identificador,cliente in listaClientes:
    
        print(identificador," - ",cliente)


match(acao):
    
    case "1":
        
        nomeCliente = input("Nome do cliente: ")
        enderecoCliente = input("Endereço do cliente: ")
        emailCliente = input("Email do cliente: ")
        telefoneCliente = input("Telefone do cliente: ")

        if (classificacao=="1"):
            
            cpnjCliente = input("CNPJ do cliente: ")

            clienteJuridico.setCnpj(cpnjCliente)
            clienteJuridico.setEmail(emailCliente)
            clienteJuridico.setEndereco(enderecoCliente)
            clienteJuridico.setNome(nomeCliente)
            clienteJuridico.setTelefone(telefoneCliente)

            clienteJuridico.setDados()
            
            dados=clienteJuridico.getDados()

            for identificador,cliente in enumerate(dados):
    
                print(identificador," - ",cliente)

            time.sleep(10)
        
    case "2":
        
        print(acao)
        
    case "3":
        
        print(acao)