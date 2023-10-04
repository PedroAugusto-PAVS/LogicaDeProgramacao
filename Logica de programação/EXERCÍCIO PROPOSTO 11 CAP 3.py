#11) Faça um programa que calcule e mostre a área de um losango.
#Sabe-se que: A = (diagonal maior * diagonal menor)/2.

D = float(input("Informe a diaonal maior do losango: "))
print()
d = float(input("Informe a diaonal menor do losango: "))
A = (D * d)/2
print()
print("--------------- REPRESENTAÇÃO MATEMÁTICA --------------")
print()
print(f" A = {D} * {d} / 2\n A = {A}")
print()
print("--------------- RESPOSTA ESCRITA --------------")
print()
print(f" A área do losango é {A}cm2.")
