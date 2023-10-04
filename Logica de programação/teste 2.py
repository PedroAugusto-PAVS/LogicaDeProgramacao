# codigo para calcular media. aula dia 18/03/22#

#p1 significa prova 1#
#p2 significa prova 2#
#mf significa média final#

nomedoaluno = input("Nome do aluno:")
print()
p1 = float(input("Digite a nota da prova 1:"))
print()
p2 = float(input("Digite a nota da prova 2:"))
mf = (p1 + p2) / 2
print()
print("A media final do",nomedoaluno, "é:", mf)
print()
if mf > 60 :
    print("Aluno aprovado!")
elif mf == 60:
    print("O Aluno passou por pouco!")
else:
    print ("Aluno reprovado!")


