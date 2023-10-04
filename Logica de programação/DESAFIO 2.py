#2) Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o
#valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre a
#relação de notas necessárias. Por exemplo:
#Entrada: R$ 576,00
#Saída:
#5 nota(s) de R$ 100,00
#1 nota(s) de R$ 50,00
#1 nota(s) de R$ 20,00
#0 nota(s) de R$ 10,00
#1 nota(s) de R$ 5,00
#0 nota(s) de R$ 2,00
#1 nota(s) de R$ 1,00

valor_int = int(input("Digite o valor inteiro que deseja sacar: "))

nota_de_cem = valor_int // 100
resto_de_cem = valor_int % 100

nota_de_cinquenta = resto_de_cem // 50
resto_de_cinquenta = resto_de_cem % 50

nota_de_vinte = resto_de_cinquenta // 20
resto_de_vinte = resto_de_cinquenta % 20

nota_de_dez = resto_de_vinte // 10
resto_de_dez = resto_de_vinte % 10

nota_de_cinco = resto_de_dez // 5
resto_de_cinco = resto_de_dez % 5

nota_de_dois = resto_de_cinco // 2
resto_de_dois = resto_de_cinco % 2

nota_de_um = resto_de_dois // 1
resto_de_um = resto_de_dois % 1

print()
print(f"Você receberá:\n{nota_de_cem} nota(s) de R$ 100,00\n{nota_de_cinquenta} nota(s) de R$ 50,00\n{nota_de_vinte} nota(s) de R$ 20,00\n{nota_de_dez} nota(s) de R$ 10,00\n{nota_de_cinco} nota(s) de R$ 5,00\n{nota_de_dois} nota(s) de R$ 2,00\n{nota_de_um} nota(s) de R$ 1,00")
