'''
Combinations, permutations e products = Itertools
Combinação - ordem não importa
Permutação - Ordem importa
Ambos não repetem valores unicos
Produto - Ordem importa e repete valores unicos
'''
from itertools import combinations, count, permutations, product

pessoa = ['Luiz', 'André', 'Ana', 'Eduardo', 'Fabio', 'Rose']

for grupo in combinations(pessoa, 2):
    print(grupo)

print()

for grupo in permutations(pessoa, 2):
    print(grupo)

print()

for grupo in product(pessoa, repeat=2):
    print(grupo)
