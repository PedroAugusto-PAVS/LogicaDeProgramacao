from dataclasses import dataclass 


@dataclass 


class MEDICO:
    Nome: str
    Rg: int
    Cpf: int
    Telefone: int
    Sexo: str
    Idade: int
    Especialidade: str


@dataclass 
class PACIENTE:
    NomeP: str
    RgP: int
    CpfP: int
    TelefoneP: int
    SexoP: str
    IdadeP: int
    EspecialidadeP: str




def CadastrarMedico(cadastrarM):
    while True:
            Nome = input("Nome do Medico ou fim para sair: ").capitalize().strip()
            if Nome == "Fim":
                break
            Rg = int(input("RG do Medico: "))
            Cpf = int(input("CPF do Medico: "))
            Telefone = int(input("Telefone do Medico: "))
            while True:
                Sexo = input("Sexo M/F: ").strip().upper()
                if Sexo == "M" or Sexo == "F":
                    break
                else:
                    print("\nERRO! DIGITE APENAS M OU F PARA SEXO.")
            Idade = int(input("Idade: "))
            Especialidade = input("Especialidade: ")
            print()
            cadastrarM.append(MEDICO(Nome, Rg, Cpf, Telefone, Sexo, Idade, Especialidade))


def CadastrarPaciente(cadastrarP):
    while True:
            NomeP = input("Nome do Paciente ou fim para sair: ").capitalize().strip()
            if NomeP == "Fim":
                break
            RgP = int(input("RG do Paciente: "))
            CpfP = int(input("CPF do Paciente: "))
            TelefoneP = int(input("Telefone do Paciente: "))
            while True:
                SexoP = input("Sexo M/F: ").strip().upper()
                if SexoP == "M" or SexoP == "F":
                    break
                else:
                    print("\nERRO! DIGITE APENAS M OU F PARA SEXO.")
            IdadeP = int(input("Idade: "))
            EspecialidadeP= input("Area da Consulta: ")
            print()
            cadastrarP.append(PACIENTE(NomeP, RgP, CpfP, TelefoneP, SexoP, IdadeP, EspecialidadeP))


def deletarM(cadastrarM):
    achou = False
    for x in range (len(cadastrarM)):
        nome = input("Nome do Medico que deseja excluir: ").capitalize().strip()
        if nome == cadastrarM[x].Nome:
            achou = True                
            break 
    if achou:
        del(cadastrarM[x])
        print("\nMedico excluido!\n")
    else:
        print("\nMedico não encontrado.\n")


def deletarP(cadastrarP):
    achou = False
    for x in range (len(cadastrarP)):
        nome = input("Nome do Paciente que deseja excluir: ").capitalize().strip()
        if nome == cadastrarP[x].NomeP:
            achou = True                
            break 
    if achou:
        del(cadastrarP[x])
        print("\nPaciente excluido!\n")
    else:
        print("\nPaciente não encontrado.\n")


def mostrarM(m):
    for x in range (len(m)):
        print()
        print(f"Medico: {m.Nome[x]}, CPF: {m.Cpf[x]}, RG: {m.Rg[x]}, Telefone: {m.Telefone[x]}, Sexo: {m.Sexo[x]}, Idade: {m.Idade[x]}, Especialidade: {m.Especialidade[x]}\n")


def mostrarP(p):
    for x in range (len(p)):
        print()
        print(f"Medico: {p.NomeP[x]}, CPF: {p.CpfP[x]}, RG: {p.RgP[x]}, Telefone: {p.TelefoneP[x]}, Sexo: {p.SexoP[x]}, Idade: {p.IdadeP[x]}, Especialidade: {p.EspecialidadeP[x]}\n")


def agenda(cadastrarM,cadastrarP):
    achou = False
    for x in range (len(cadastrarM)):
        nome = input("Nome do Medico que deseja ver a agenda: ").capitalize().strip()
        if nome == cadastrarM[x].Nome:
            achou = True                
            break 
    if achou:
        print(f"Medico: {cadastrarM[x].Nome}\n")
        for j in range (len(cadastrarP)):
            if cadastrarP[j].EspecialidadeP == cadastrarM[j].Especialidade:
                print(f"Paciente: {cadastrarP[j].NomeP}")
    else:
        print("Medico não Encontrado!")


def titulo(txt):
    print("-" *30 )
    print(txt)
    print("-" * 30)
