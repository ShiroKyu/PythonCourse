from dados import produtos, pessoas, lista
from functools import reduce

somaLista = reduce(lambda ac, e: e + ac, lista, 0)

print(somaLista)


##################
def catchPrices(p): return p['preco']


somaPrecos = list(map(catchPrices, produtos))

somaPrecos = reduce(lambda ac, e: ac + e, somaPrecos, 0)
print(somaPrecos)
