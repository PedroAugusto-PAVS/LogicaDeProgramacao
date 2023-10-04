'''
produto | preço | quantidade | valor
-------------------------------------
        |       |            |
-------------------------------------
        |       |            |
-------------------------------------
MENU:
    1 - CADASTRAR VENDA # INSERIR NA MATRIZ PRODUTO, PREÇO, QUANTIDADE E VALOR
    2 - PESQUISAR PRODUTO # SE EXISTIR, MOSTRAR PREÇO, QUANTIDADE E VALOR
    3 - RELATÓRIO GERAL # TUDO QUE FOI VENDIDO MOSTRANDO PREÇO, QTD E VALOR
    4 - REMOVER VENDA # EXCLUIR UMA LINHA INTEIRA DA MATRIZ
    5 - PRODUTO MAIS CARO # MAIOR VALOR DA SEGUNDA COLUNA
    6 - PRODUTO MAIS VENDIDO # MAIOR VALOR DA PENÚLTIMA COLUNA
    7 - VALOR TOTAL DA VENDA # SOMATÓRIO DA ÚLTIMA COLUNA
    0 - SAIR

'''

from moduloVendas import *
from titulo import *


matrizvendas=[]

while True:
    titulo('1 - CADASTRAR VENDA\n2 - PESQUISAR PRODUTO\n3 - RELATÓRIO GERAL\n4 - REMOVER VENDA\n5 - PRODUTO MAIS CARO\n6 - PRODUTO MAIS VENDIDO\n7 - VALOR TOTAL DA VENDA\n0 - SAIR')
    print()
    op=input("Digite a opção: ")
    print()
    if op=='0':
        break
    elif op=='1':
        titulo('CADASTRO DE PRODUTO')
        cadastro(matrizvendas)
    elif op=='2':
        titulo('PESQUISA DE PRODUTO')
        pesquisa(matrizvendas)
    elif op=='3':
        titulo('RELATÓRIO GERAL')
        print(matrizvendas,"\n")
    elif op=='4':
        titulo('REMOVER VENDA')
        remover(matrizvendas)
    elif op=='5':
        titulo('PRODUTO MAIS CARO')
        maiorProduto(matrizvendas)
    elif op=='6':
        titulo('PRODUTO MAIS VENDIDO')
        maiorVendido(matrizvendas)
    elif op=='7':
        titulo('VALOR TOTAL DA VENDA')
        totalVenda(matrizvendas)
    else:
        print('\nOPÇÃO INVÁLIDA! DIGITE UM VALOR DE 0 A 7!\n')
