def parni(list):
    recnik = {
        'Parni': [],
        'Neparni': []
    }
    for item in list:
        if(item % 2 == 0):
            recnik['Even: '].append(item)
        else:
            recnik['Odd'].append(item)
    return(recnik)

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

def numlista(lista):
    tipovi = {}
    for item in lista:
        if type(item).__name__ not in tipovi:
            tipovi[type(item).__name__] = []
            tipovi[type(item).__name__].append(item)
        else:
            tipovi[type(item).__name__].append(item)
    return(tipovi)

def uredi(lista, n, m):
    for i in range(0, n):
        lista[i] += m
    for i in range(n, len(lista)):
        lista[i] -= m
    return lista

def zbir(lista):
    prazna = []
    for i in range(0, len(lista) - 1):
        prazna.append(lista[i] + lista[i+1])
    return prazna

def brojel(lista):
    prazna = []
    for item in lista:
        if(type(item).__name__ == 'list'):
            prazna.append(len(item))
        else:
            prazna.append(-1)
    return prazna

def razlika(lista1, lista2):
    prazna = []
    for item in lista1:
        if item not in lista2:
            prazna.append(item)
    return prazna

def saberi(lista):
    prazna = []
    suma = 0
    for item in lista:
        for subitem in item:
            suma += subitem
        prazna.append(suma)
        suma = 0
    return prazna

def izmeni(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
        lista[i] = suma
    return lista

def prosek(lista):
    prazna = []
    prosek = 0
    for item in lista:
        for subitem in item:
            prosek += subitem
        prosek /= len(item)
        prazna.append(prosek)
        prosek = 0
    return prazna

#def izbroj(lista):



zadatak1 = [1, 2, 3, 4, 5]; #prvizadatak = list(range(1,6))

zadatak2 = ["Prvi", "Drugi", 2, 4, [3, 5]]

zadatak3 = list(range(1, 6))

zadatak4 = list(range(1, 6))

zadatak5 = [[1, 2], [3, 4, 5], 'el', ['1', 1]]

zadatak6_1 = [1, 4, 6, "2", "6"]
zadatak6_2 = [4, 5, "2"]

zadatak7 = [(1, 4, 6), (2, 4), (4, 1)]

zadatak8 = [1, 2, 4, 7, 9]

zadatak9 = [[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]

zadatak16 = {
    1 : 4,
    2 : [2, 3], 
    3 : [5, 6], 
    4 : 'test', 
    5 : 9, 
    6 : 8
}

print(prosek(zadatak9))