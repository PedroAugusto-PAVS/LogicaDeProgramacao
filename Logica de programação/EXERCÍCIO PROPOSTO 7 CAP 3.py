#7) Faça um programa que receba o peso de uma pessoa, calcule e mostre:
#a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
#b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

peso1 = float(input("Digite o peso da pessoa: "))

#np é o novo peso em 15%
np = peso1 + (peso1 * (15/100))
#np2 é o novo peso em 15%
np2 = peso1 - (peso1 * (20/100))

print()
print("----------- INFORME DOS NOVOS PESOS -------------")
print(f" O novo peso, se a pessoa engordar 15% sobre o peso digitado é de {np}kg.")
print()
print(f" O novo peso, se a pessoa emagrecer 20% sobre o peso digitado é de {np2}kg.")
