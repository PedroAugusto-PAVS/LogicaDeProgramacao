#3) FAÇA UM PROGRAMA QUE RECEBA TRÊS NOTAS E SEUS RESPECTIVOS PESOS, CALCULE E MOSTRE A MÉDIA PONDERADA.#
#n1 significa nota 1#
#n2 significa nota 2#
#n3 significa nota 3#
#p1 significa peso 1#
#p2 significa peso 2#
#p3 significa peso 3#
#m1 significa multiplicação 1#
#m2 significa multiplicação 2#
#m3 significa multiplicação 3#
#sp significa soma dos pesos#
#mp significa média ponderada#

n1 = float(input("Informe a primeira nota:"))
p1 = float(input("Informe o peso da primeira nota:"))
print()#print para pular uma linha#
n2 = float(input("Informe a segunda nota:"))
p2 = float(input("Informe o peso da segunda nota:"))
print()#print para pular uma linha#
n3 = float(input("Informe a terceira nota:"))
p3 = float(input("Informe o peso da terceira nota:"))

m1 = n1 * p1
m2 = n2 * p2
m3 = n3 * p3
sp = p1 + p2 + p3
mp = (m1 + m2 + m3)/sp
print()#print para pular uma linha#
#o primeiro print é so um exemplo de como poderia ser feito a media sem precisar atribuir mp#
print("A média ponderada das notas é:", ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3))
print("A média ponderada das notas é:", mp)
