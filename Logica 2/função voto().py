def voto(anonas):
    """
    :param anonas: recebe o ano em que a pessoa nasceu.
    :return: os returns são para retornar a condição de voto do eleitor.
    Um exemplo é o return "NEGADO", que retorna a mensagem "NEGADO" para o programa
    principal.

    """
    from datetime import date
    atual = date.today().year
    idade = atual-anonas

    if idade < 16:
        return f"Com {idade} anos o eleitor tem voto NEGADO."
    elif 16 <= idade > 18 or idade>65: #modo de dizer que idade está de 16 até 18 ou maior que 65.
        return f"Com {idade} anos o eleitor tem voto OPCIONAL."
    elif idade>=18:
        return f"Com {idade} anos o eleitor tem voto OBRIGATÓRIO."



#Programa Principal
ano = int(input("Digite a data de Nascimento da Pessoa: "))
print(voto(ano))
