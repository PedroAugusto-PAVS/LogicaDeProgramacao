@dataclass

class Venda:
    Produto: str
    Preco: float
    Quantidade: int
    Valor: float 
def CADASTRO(x, tipo):
    while True:
            Produto= input("Nome do Produto: ")
            if Produto=="FIM":
                break
            Preco= float(input("Preço do Produto: "))
            Quantidade= int(input("Quantidade do Produto: "))
            Valor= Preco*Quantidade
            x.append(tipo(Produto,Preco, Quantidade,Valor))

def PESQUISA():
    achou=False
        for i in range(len(x)):
            nome=input("Nome do Produto a ser pesquisado: ")
            if nome==x[i].Venda:
                achou=True
            if achou:
                print(f"\nnome\n")
            else:
                print("\nProduto não encontrado na venda\n")

def GERAL():
    print(x,"\n")

def EXCLUIR():
    achou=False
        for i in range(len(x)):
            nome=input("Nome do Produto a ser excluido: ")
            if nome==x[i].Venda:
                achou=True
            if achou:
                print("\nProduto Excluido\n")
            else:
                print("\nProduto não encontrado na venda\n")          
