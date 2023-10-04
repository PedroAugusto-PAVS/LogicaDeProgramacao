#4)Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira e peso 3 para a segunda.#
#n1 significa número 1#
#n2 significa número 2#
#p1 significa peso 1#
#p2 significa peso 2#


n1 = float(input("Informe o primeiro número:"))
p1 = 2
n2 = float(input("Informe o segundo número:"))
p2 = 3
print()#print para pular uma linha#

print("A media ponderada dos números é:", ((n1*p1)+(n2*p2))/(p1+p2) )
