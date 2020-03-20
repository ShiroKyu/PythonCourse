'''
Zip - Unindo iteráveis
Zip_longest - Intertools
'''

from itertools import zip_longest, count

# Código

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Pico da agulha']
estados = ['SP', 'MG', 'BA', 'AM']

cidadesEstados = zip(cidades, estados)  # retorna um iterador

for valor in cidadesEstados:
    print(valor[0], valor[1])
print()
# também pode ser convertido em lista ou dicionario // [('São paulo', 'SP'), ('Belo horizontes', 'MG')...]
# cidadesEstados = list(cidadesEstados)


#####################################
indice = count()
cidades2 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Pico da agulha']
estados2 = ['SP', 'MG', 'BA']

# Preenche com nome o que faltar, para setar valor padrão: fillValue
cidadeEstados2 = zip_longest(indice, cidades2, estados2, fillvalue='Estado')
