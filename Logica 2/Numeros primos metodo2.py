def primo (n):
    c = 0
    for x in range(1, n):
        resto = n%x
        if resto == 0:
            c += 1
        if c > 1:
            break
    if c == 1:
        return True
    else:
        return False
num=(int(input("Digite um numero: ")))
primo(num)
print(primo(num))
if primo(num)== True:
    print("O numero é primo")
if primo(num)== False:
    print("O numero não é primo")

