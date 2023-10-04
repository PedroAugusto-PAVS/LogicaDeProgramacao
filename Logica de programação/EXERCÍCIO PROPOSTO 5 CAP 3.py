#5) Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se
#que este sofreu um desconto de 10%.
print("-----------QUAL O PREÇO DO PRODUTO?-------------")
precoProduto = float(input("Informe o preço do produto: "))

# desconto 10%:
desconto = precoProduto * 0.1
#desconto de 10% aplicado no produto:
descontoAplicado = precoProduto - desconto
print()
print("-----------PRODUTO COM DESCONTO-------------")
print(f"O produto vai ficar R${descontoAplicado} após sofrer o desconto.")
