#1) Escreva um programa para calcular a redução do tempo de vida de um fumante.Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba
#o total em dias.
#minutos_por_cigarro é para saber quantos minutos de vida ao todo o usuario perde fumando.
#dias_fumando é para saber quantos dias ele fumou(conversão de anos para dias).

quantidade_de_cigarros = int(input("Quantidade de cigarros fumados por dia: "))
print()
anos_fumando = float(input("Quantidade de anos fumando: "))

minutos_por_cigarro = (quantidade_de_cigarros * 10)

dias_fumando = anos_fumando * 365

dias_perdidos = minutos_por_cigarro * dias_fumando //(24*60) #24*60 é a quantidade de minutos que um dia tem.
print()
print(f"O fumante perdeu {dias_perdidos} dias")


