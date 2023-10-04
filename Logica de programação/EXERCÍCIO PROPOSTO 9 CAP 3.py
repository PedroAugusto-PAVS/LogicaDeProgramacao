#9) Faça um programa que calcule e mostre a área de um trapézio.
#Sabe-se que: A = ((base maior + base menor) * altura)/2

B = float(input("Informe a base maior do trapézio: "))
print()
b = float(input("Informe a base menor do trapézio: "))
print()
h = float(input("Informe a altura do trapézio: "))
A = ((B + b) * h)/2
print()
print("--------------- REPRESENTAÇÃO MATEMÁTICA --------------")
print()
print(f" A = (({B} + {b}) * {h})/2\n A = {A}")
print()
print("--------------- RESPOSTA ESCRITA --------------")
print()
print(f" A área do trapézio é {A}cm2.")
