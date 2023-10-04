from funções import *
 
m = []
p = []

while True:
    titulo("MENU DE OPÇÕES")
    print("OPÇÃO 0 = SAIR\nOPÇÃO 1 = CADASTRAR MEDICO\nOPÇÃO 2 = CADASTRAR PACIENTE\nOPÇÃO 3 = DELETAR MEDICO\nOPÇÃO 4 = DELETAR PACIENTE\nOPÇÃO 5 = MOSTRAR MEDICOS\nOPÇÃO 6 = MOSTRAR PACIENTES\nOPÇÃO 7 = MOSTRAR AGENDA DO MEDICO\n")
    op = input("OPÇÃO: ")
    if op == "0":
        break
    if op == "1":
        titulo("CADASTRO DE MEDICO")
        CadastrarMedico(m) 
    if op == "2":
        titulo("CADASTRO DE PACIENTE")
        CadastrarPaciente(p)
    if op == "3":
        titulo("DELETAR MEDICO")
        deletarM(m)
    if op == "4":
        titulo("DELETAR PACIENTE")
        deletarP(p)
    if op == "5":
        titulo("MEDICOS")
        print(m)
        #mostrarM(m)
    if op == "6":
        titulo("PACIENTES")
        print(p)
        #mostrarP(p)
    if op == "7":
        titulo("AGENDA DO MEDICO")
        agenda(m,p)