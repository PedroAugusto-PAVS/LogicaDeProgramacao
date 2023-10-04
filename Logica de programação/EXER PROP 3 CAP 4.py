#3) Faça um programa que receba dois números e mostre o menor.

n1 = float(input("Digite numero 1: "))
n2 = float(input("Digite numero 2: "))

if n1 > n2 :
    print(f"O numero menor é {n2:.0f}")
elif n1 < n2 :
    print(f"O numero menor é {n1:.0f}")
else:
    print("Os numeros são iguais.")
