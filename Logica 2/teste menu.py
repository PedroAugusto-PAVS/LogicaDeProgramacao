'''
produto | preÃ§o | quantidade | valor
-------------------------------------
        |       |            |
-------------------------------------
        |       |            |
-------------------------------------
MENU:
    1 - CADASTRAR VENDA # INSERIR NA MATRIZ PRODUTO, PREÃ‡O, QUANTIDADE E VALOR
    2 - PESQUISAR PRODUTO # SE EXISTIR, MOSTRAR PREÃ‡O, QUANTIDADE E VALOR
    3 - RELATÃ“RIO GERAL # TUDO QUE FOI VENDIDO MOSTRANDO PREÃ‡O, QTD E VALOR
    4 - REMOVER VENDA # EXCLUIR UMA LINHA INTEIRA DA MATRIZ
    5 - PRODUTO MAIS CARO # MAIOR VALOR DA SEGUNDA COLUNA
    6 - PRODUTO MAIS VENDIDO # MAIOR VALOR DA PENÃšLTIMA COLUNA
    7 - VALOR TOTAL DA VENDA # SOMATÃ“RIO DA ÃšLTIMA COLUNA
    0 - SAIR

'''
from moduloVendas import *

while True:
    print('1 - CADASTRAR VENDA\n2 - PESQUISAR PRODUTO\n3 - RELATÃ“RIO GERAL\n4 - REMOVER VENDA\n5 - PRODUTO MAIS CARO\n6 - PRODUTO MAIS VENDIDO\n7 - VALOR TOTAL DA VENDA\n0 - SAIR')

    op=input()
    if op=='0':
        break
    elif op=='1':
        print('CADASTRO DE PRODUTO')
        cadastro()
    elif op=='2':
        print('PESQUISA DE PRODUTO')
    elif op=='3':
        print('RELATÃ“RIO GERAL')
    elif op=='4':
        print('REMOVER VENDA')
    elif op=='5':
        print('PRODUTO MAIS CARO')
    elif op=='6':
        print('PRODUTO MAIS VENDIDO')
    elif op=='7':
        print('VALOR TOTAL DA VENDA')
    else:
        print('OPÃ‡ÃƒO INVÃLIDA! DIGITE UM VALOR DE 0 A 7!')