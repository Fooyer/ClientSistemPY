# Este arquivo será executado para fazer operações nos dados

import os
from Dados.clienteFisico import clienteFisico
from Dados.clienteJuridico import clienteJuridico

os.system('clear')

acao = input("Qual ação deseja efetuar? \n\n 1 - Cadastrar novo cliente \n 2 - Excluir cliente \n 3 - Editar cliente \n\n Resposta: ")

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
        exit()

classificacao = input("\n\n"+descricaoAcao+" cliente: \n\n 1 - Jurídico \n 2 - Físico \n\n Resposta: ")

match(acao):
    
    case "1":
        
        print(acao)
        
    case "2":
        
        print(acao)
        
    case "3":
        
        print(acao)