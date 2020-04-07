from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'C'},
    {'nome': 'Rose', 'nota': 'B'},
    {'nome': 'Mary', 'nota': 'A'},
    {'nome': 'Elise', 'nota': 'A'},
    {'nome': 'Diane', 'nota': 'D'},
    {'nome': 'Chariot', 'nota': 'A'},
    {'nome': 'John', 'nota': 'B'},
    {'nome': 'Frank', 'nota': 'B'},
    {'nome': 'James', 'nota': 'C'}
]


def ordena(x): return x['nota']


alunos.sort(key=ordena, reverse=False)

for aluno in alunos:
    print(f'{aluno["nome"]}, {aluno["nota"]}')

alunos_ordenados = groupby(alunos, ordena)
chaves = []
grupos = []


for key, group in alunos_ordenados:  # alunos_ordenados é uma tupla, 'group' é um iterável de varios dicionarios de alunos no caso
    # [('A', <itertools._grouper object at 0x7f4f8002ed50>), ...]
    print(f'Agrupamento {key}:')
    chaves.append(key)

    for g in group:
        print(g)
        grupos.append(g)

    quantidade = len(list(group))
    # quantidade = len(list(group)), se tentar declarar a quantidade depois do for, o 'group' terá se esgotado, dando
    # como resultado da 'len' 0
    print(quantidade)

print(chaves, grupos)
