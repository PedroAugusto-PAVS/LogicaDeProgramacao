#programa para saber se o numero é impar ou par

num = int(input("Digite um numero: "))
resto = num % 2
print()
if resto == 0:
    print("numero par")
else:
    print("numero ímpar")
