'''
count - itertools
'''
from types import GeneratorType
from itertools import count

variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
print(isinstance(variavel, GeneratorType))

contador = count(start=5, step=0.1)  # gera um iterador

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break

print()
novoContador = count(start=1, step=0.5)
for i in novoContador:
    print(i)
    if i == 50:
        break

print()
lista = ['João', 'Maria', 'Paulo']
maisUmCont = count(start=0, step=1)
lista = list(zip(maisUmCont, lista))

for indice, nome in lista:
    print(f'{indice}: {nome}')

print(dict(lista))
