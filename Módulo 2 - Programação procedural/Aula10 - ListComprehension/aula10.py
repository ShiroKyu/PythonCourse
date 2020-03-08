l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [var for var in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l2]
print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]
print(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 5 == 0 if v % 3 == 0]
print(ex6)

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)
