def titulo(txt):
    tam = len(txt) + 2
    print()
    print("~" * tam)
    print(f"  {txt}")
    print("~" * tam)
    print()

def area(base, altura):
    a = base * altura
    titulo(f"A área do seu terreno de {base}X{altura}M é de {a}m^2.")

#Programa Principal:
titulo("Controle de Terrenos")
titulo("Tela de Login")
while True:
    user = input("Usuário: ")
    print()
    senha = input("Senha: ")
    if user == "20221050100070" and senha == "Teste0202$" :
        break
    print("\nUsuário ou senha errados! Tente Novamente com os certos.\n")

titulo("Medidas")
b = float(input("Informe a largura: "))
print()
h = float(input("Informe a altura: "))
area(b,h)

    
