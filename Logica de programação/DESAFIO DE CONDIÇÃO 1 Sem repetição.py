#No caminho para encontrar Jon Snow em Dragonstone, o lobo Ghost enfrenta um problema, uma grande escada. As escadas
#são numeradas de 1 ate infinito. Sendo um lobo esperto, Ghost decidiu calcular dois valores, o número de
#escadas percorridas com números pares e ímpares. Você precisa checar se o número de passos em escadas pares e ímpares
#encontrados pelo Ghost estão corretos. Considere que ele não pula nenhuma escada e que ele sobe, pelo menos, a escada de número 1.


#se de 1 ate 10 tem 5 impares e 5 pares então a cada 10 numeros 5 seriam pares e 5 impares.
#exemplo de 1 ate 10:
#pares: 2,4,6,8,10 = 5 numeros
#impares: 1,3,5,7,9 = 5 numeros
#sendo assim a cada 9 numeros 5 seriam impares e 4 seriam pares.
#exemplo de 1 ate 9:
#pares: 2,4,6,8 = 4 numeros
#impares: 1,3,5,7,9 = 5 numeros


esc = int(input("Quantas escadas o Ghost subiu?\n>>>>> " ))

if esc%2 == 0:
    print(f"""Ele subiu {esc//2} escadas pares e
{esc // 2} escadas impares.""")
    print()
    print("------//-----" * 5)
    print()
elif esc%2 != 0 and esc != 1:
    print(f"""Ele subiu {esc//2} escadas pares e
{ (esc + 1) // 2} escadas impares.""")
    print()
    print("------//-----" * 5)
    print()
else:
    print(f"ele subiu 1 escada impar." )
    print()
    print("------//-----" * 5)
    print()

