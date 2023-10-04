from dataclasses import dataclass
from titulo import *
@dataclass

class Venda:
    Produto: str
    Preco: float
    Quantidade: int
    Valor: float 


x=[]
while True:
    
    titulo("MENU DE VENDAS:")
    print("OPÇÃO #0 = SAIR\nOPÇÃO #1 = CADASTRO DE VENDA\nOPÇÃO #2 = PESQUISA DE PRODUTO\nOPÇÃO #3 = IMPRIMIR O GERAL DE VENDAS\nOPÇÃO #4 = DELETAR PRODUTO")
    op=input("digite a opção: ")
    print()
 
    if op=="0":
        break 

    if op=="1":
        while True:
            Produto= input("Nome do Produto: ")
            if Produto=="FIM":
                break
            Preco= float(input("Preço do Produto: "))
            Quantidade= int(input("Quantidade do Produto: "))
            Valor= Preco*Quantidade
            x.append(Venda(Produto,Preco, Quantidade,Valor))

    elif op=="2":
        achou=False
        for i in range(len(x)):
            nome=input("Nome do Produto a ser pesquisado: ")
            if nome==x[i].Produto:
                achou=True
                break
        if achou:
            print(f"\n{nome}\n")
            print("\nProduto Encontrado\n")
        else:
            print("\nProduto não encontrado na venda\n")

    elif op=="3":
        print(x,"\n")
    
    elif op=="4":
        achou=False
        for i in range(len(x)):
            nome=input("Nome do Produto a ser excluido: ")
            if nome==x[i].Produto:
                achou=True
                break
        if achou:
            del(x[i])
            print("\nProduto Excluido\n")
        else:
            print("\nProduto não encontrado na venda\n")          

