#12) Faça um programa que receba o valor do salário mínimo e o valor do
#salário de um funcionário, calcule e mostre a quantidade de salários mínimos
#que esse funcionário ganha.

salmin = float(input("Informe o salário mínimo: "))
print()
salario = float(input("Informe o salário do funcionário: "))

quant_sal = salario / salmin

print()
print("--------------- // --------------")
print()
print(f" O funcionário recebe {quant_sal:.1f} salário(s) mínimo(s).")
