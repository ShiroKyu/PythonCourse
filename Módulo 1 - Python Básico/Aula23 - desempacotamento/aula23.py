"""
Desempacotamento de listas em python

"""

# Desempacotamento
lista = ['Paulo', 'Luiz', 'Maria']
n1, n2, n3 = lista

print(n1, n2, n3)

lista2 = ['Paulo', 'Luiz', 'Maria', 1, 2, 3, 4, 5]
var1, var2, *outraLista = lista2

print(var1, var2, outraLista)

# Pegando também o ultimo valor
lista3 = ['Paulo', 'Luiz', 'Maria', 1, 2, 3, 4, 5]
var1, var2, *outraLista, ultimoValor = lista2

print(var1, var2, outraLista, ultimoValor)

# Pegando apenas primeiros valores
lista4 = ['Paulo', 'Luiz', 'Maria', 1, 2, 3, 4, 5]
var1, var2, *_ = lista4  # "*_" indica que o resto dos valores não serão usados

print(var1, var2)
