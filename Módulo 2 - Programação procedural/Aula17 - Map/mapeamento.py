from dados import produtos, pessoas, lista

# Não retorna uma lista pronta, retorna um iterador
# novaLista = map(lambda x: x * 2, lista)
novaLista = [x * 2 for x in lista]  # Forma mais interessante de se fazer
print(novaLista)


def aumentaPreco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novosProdutos = map(aumentaPreco, produtos)

for produto in novosProdutos:
    print(produto)
