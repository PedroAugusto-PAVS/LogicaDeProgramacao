#7)  Uma empresa decide dar um aumento de 30% aos funcionários com salários inferiores a R$ 500,00. Faça um
#programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, caso
#ele não tenha direito ao aumento.

sal = float(input("Informe o salário do funcionario: "))

if sal < 500 :
    print(f"O salário reajustado do funcionario é {sal + (sal * (30/100))}")
else:
    print("O funcionario não tem direito a um aumento.")
