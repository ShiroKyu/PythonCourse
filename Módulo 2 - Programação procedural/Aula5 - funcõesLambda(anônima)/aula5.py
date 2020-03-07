'''
Funções anonimas
'''

#  a = lambda x, y: x * y
# print(a(1, 3))

lista = [["p1", 13], ["p2", 50], ["p3", 23], ["p4", 12], ["p5", 11]]


def func(item):
    return item[1]


# sort(key, reverse) -> key=função para para especificar os criterios de busca, reverse = inverter
#lista.sort(key=func, reverse=True)

# usando função lambda
lista.sort(key=lambda item: item[1], reverse=False)
print(lista)

# Ou ordenar sem afetar a lista original
print(sorted(lista, key=lambda item: item[1], reverse=True))
