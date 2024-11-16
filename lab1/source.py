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

def izbroj(lista):
    brojac = 0
    for element in lista:
        if isinstance(element, list):
            brojac += izbroj(element)
        else:
            brojac += 1
    return brojac

def razlika(lista):
    prazna = []
    for i in range(0, len(lista) - 1):
        prazna.append(lista[i] - lista[i + 1])
    return prazna

def presek(lista1, lista2):
    prazna = []
    for item in lista1:
        if item in lista2:
            prazna.append(item)
    return prazna

def izmeni(lista):
    parni = []
    neparni = []
    for i in range(0, len(lista)):
        if i % 2 == 0:
            lista[i] += 1
            parni.append(lista[i])
        else:
            lista[i] -= 1
            neparni.append(lista[i])

    dict = {}
    dict['pp'] = parni.copy()
    dict['np'] = neparni.copy()
    return dict

def unija(lista1, lista2):
    prazna = lista1.copy()
    for item in lista2:
        if item not in lista1:
            prazna.append(item)
    return prazna

def izdvoji(lista):
    prazna = []
    n = 0
    for item in lista:
        if n < len(item):
            prazna.append(item[n])
        else:
            prazna.append(0)
        n += 1
    return prazna

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

def kreiraj(n):
    prazna = []
    brojac = 0
    for i in range(0, n + 1):
        brojac += i
        tuple = (i, brojac**2)
        prazna.append(tuple)
    return prazna

def pomoc_razlika(lista1, lista2):
    prazna = []
    for item in lista1:
        if item not in lista2:
            prazna.append(item)
    return prazna


def kreiraj2(lista):
    prazna = []
    for i in range(0, len(lista) - 1):
        prazna.append(pomoc_razlika(lista[i], lista[i + 1]))
    return prazna

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

zadatak10 = [1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]

zadatak11 = [8, 5, 3, 1, 1]

zadatak12_1 = [1, 5, 4, "1", "8", 3, 7]
zadatak12_2 = [1, 9, "1"]

zadatak13 = [8, 6, 3, 1, 1]

zadatak14_1 = [5, 4, "1", "8", 7]
zadatak14_2 = [1, 9, "1"]

zadatak15 = [[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]

zadatak16 = {
    1 : 4,
    2 : [2, 3], 
    3 : [5, 6], 
    4 : 'test', 
    5 : 9, 
    6 : 8
}

zadatak17 = 4

zadatak18 = [[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]

zadatak19 = [[(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]]

print(kreiraj2(zadatak18))