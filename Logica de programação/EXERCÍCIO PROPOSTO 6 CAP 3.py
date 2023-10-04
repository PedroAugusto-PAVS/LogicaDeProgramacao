#6) Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa
#que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu
#salário final.
salfix = float(input("Informe o salário fixo: "))
print()
valor_das_vendas = float(input("Informe o valor das vendas: "))

comissao = valor_das_vendas * (4/100)
print()
print("---------- COMISSÃO DAS VENDAS ----------")
print(f"A comissão das vendas é de R${comissao}.")
print()
print("---------- SALÁRIO FINAL ----------")
print(F"O salário final é de R${salfix + comissao}.")
