from functools import reduce
from itertools import zip_longest, starmap
import operator

primer = lambda x: x % 2 == 0 and "Paran" or "Neparan"

def poredak(lista1, lista2):
    return list(map(lambda x, y: (x, y, 'Jeste' if y / 2 == x else 'Nije'), lista1, lista2))

def spojidict(lista1, lista2):
    return list(map(lambda x: dict({'prvi': x[0], 'drugi': x[1]}), list(zip_longest(lista1, lista2, fillvalue='-'))))


def spoji(lista1, lista2):
    return list(starmap(lambda x, y: (x, y, x+y) if x<y else (y, x, x+y), zip_longest(lista1, lista2, fillvalue=0)))

def suma(lista):
    return reduce(lambda x, y: x + y, [z for z in [reduce(lambda p, q: p + q, r, 0) for r in lista]], 0)

def proizvod(lista):
    return list(map(lambda x: reduce(operator.mul, x, 1), lista)) #???

def objedini1(lista1, lista2):
    return list(starmap(lambda x, y: (x, y) if x < y else (y, x), zip_longest(lista1, lista2, fillvalue = 0)))

def objedini2(lista):
    return dict(reduce(lambda acc,el: acc | {str(el[0]): el[1:] if el[1:] else None}, lista, dict()))

def izracunaj(lista):
    return list(map(lambda x: x if type(x) == int else reduce(operator.mul, x, 1), lista))

def zamena(lista, x = 5):
    return [(lista[i] if (lista[i] >= x) else (reduce(operator.add, lista[i+1:]))) for i in range(0, len(lista))]

z1_1 = [1, 7, 2, 4]
z1_2 = [2, 5, 2]
z2_1 = [1, 7, 2, 4]
z2_2 = [2, 5, 2]
z3_1 = z2_1.copy()
z3_2 = z2_2.copy()
z4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
z5 = z4.copy()
z6_1 = [1, 7, 2, 4, 5]
z6_2 = [2, 5, 2]
z7 = [(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)]
z8 = [1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]
z9 = [1, 7, 5, 4, 9, 1, 2, 7]
z10 = [1, 5, 2, 6, 1, 6, 3, 2, 9]