l1 = [1, 2, 3]
l2 = [v ** 2 for v in l1]
print(l2)

lista = [
    ('chave', 'valor'),
    ('chave1', 'valor2')
]

d1 = {x: y for x, y in lista}
print(d1)

lista2 = [
    0, 1, 3, 4
]

lista3 = {x: y for x, y in enumerate(range(5))}

print(lista3)

lista4 = {x for x in range(5)}
print(lista4)
print(type(lista4))
