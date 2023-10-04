#14) Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
#a) a idade dessa pessoa em anos;
#b) a idade dessa pessoa em meses;
#c) a idade dessa pessoa em dias;
#d) a idade dessa pessoa em semanas.

ano_de_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
ano_atual = int(input("Digite o ano atual: "))

#fazendo os cálculos:
anos = ano_atual - ano_de_nascimento
dias = anos * 365
meses = dias // 30
semanas = dias // 7

print()
print(f"A idade dessa pessoa em anos é {anos} anos.")
print(f"A idade dessa pessoa em meses é {meses} meses.")
print(f"A idade dessa pessoa em dias é {dias} dias.")
print(f"A idade dessa pessoa em semanas é {semanas} semanas.")

