##1) Faça um programa contendo uma sub-rotina que retorne 1 se o número digitado for positivo ou 0 se
##for negativo.

def verifica(n):
    if n > 0 :
        res = 1
    else:
        res = 0
    return res

#Programa Principal
num = int(input("digite um numero"))

if  num ==0:
    print("negativo")
else:
    print("positivo")
