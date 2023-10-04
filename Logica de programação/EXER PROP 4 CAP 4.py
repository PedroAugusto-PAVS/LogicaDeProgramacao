#4) Faça um programa que receba três números e mostre o maior. 

n1 = float(input("Digite numero 1: "))
n2 = float(input("Digite numero 2: "))
n3 = float(input("Digite numero 3: "))

if n1 == n2 and n2 == n3:
    print("os numeros são iguais.")
elif n1 >= n2 and n1 >= n3:
    print(f"O numero maior é {n1:.0f}")
elif n2 >= n1 and n2 >= n3:
    print(f"O numero maior é {n2:.0f}")
elif n3 >= n1 and n3 >= n2:
    print(f"O numero maior é {n3:.0f}")
else:
    print("Aconteceu Um Erro Inválido.")
