from functools import reduce
import operator

def izracunaj(lista):
    return list(map(lambda x: x if type(x) == int else reduce(operator.mul, x, 1), lista))

lista = [1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]
print(izracunaj(lista))