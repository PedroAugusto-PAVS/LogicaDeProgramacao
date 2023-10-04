def relogio():
    seg = int(input("digite os segundos: "))
    horas = seg//(60**2)
    resto_h = seg%(60**2)
    minutos = resto_h//60
    segundos = resto_h%60
    

    print(f"{horas}h, {minutos}m, {segundos}s")

relogio()
