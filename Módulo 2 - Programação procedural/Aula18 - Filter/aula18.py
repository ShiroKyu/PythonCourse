from dados import produtos, pessoas, lista

# Retorna um iterador
novaLista = list(filter(lambda item: item > 5, lista))

# Com list compreheension
novaLista2 = [x for x in lista if x > 5]

print(novaLista2)

novosProdutos = filter(lambda p: p['preco'] > 10, produtos)

for p in novosProdutos:
    print(p)


def filtra(p): return p['preco'] > 50


for i in produtos:
    print(filtra(i))
