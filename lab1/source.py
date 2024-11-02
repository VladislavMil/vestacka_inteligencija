def brojanje(d):
    tipovi = {}
    for vrednost in d.values():
        tip_vrednosti = type(vrednost).__name__
        if tip_vrednosti in tipovi:
            tipovi[tip_vrednosti] += 1
        else:
            tipovi[tip_vrednosti] = 1
    rezultat = []
    for i in tipovi.items():
        rezultat.append(i)
    return rezultat

dict = {
    1 : 4,
    2 : [2, 3], 
    3 : [5, 6], 
    4 : 'test', 
    5 : 9, 
    6 : 8
}

print(brojanje(dict))

