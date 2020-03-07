import copy
d1 = {'Chave1': 'Valor da chave', 'Idade': 18}
d1['OutraChave'] = 'OutroValor'
print(d1)
print(d1['Chave1'])

d2 = dict(chave1='PrimeiraChave', chave2='SegundaChave')
print(d2)

d3 = {'Valor': 1, 'valor': 2, 'valor': 3}  # As chaves precisam ser únicas
print(d3)

d4 = {
    'str': 'valor',
    123: 'outroValor',
    (1, 2, 3): 'Tupla'
}  # Pode ser usado qualquer valor imutável como chave

if d4.get(123) is not None:
    print(d4)

d4.update({'MaisUmaChave': '1010'})
print(d4)

del d4['MaisUmaChave']
print(d4)

print('str' in d4)
print('valor' in d4.values())
print(len(d4))


# Iterações
for k in d4:
    print(k)

for k in d4.items():
    print(k)

print('')

# ------

clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio'
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
print('')

# --- Cópia rasa de dicionário

'''
d5 = {1: 'Chave1', 2: 'Chave2', 3: 'Chave3'}
v = d5.copy()
d5[1] = 'ChaveAlterada'
print(d5)
print(v)
'''
d5 = {1: 'Chave1', 2: 'Chave2', 3: 'Chave3'}
v = copy.deepcopy(d5)
v[3] = 'ChaveAlt'
print(d5)
print(v)

print('')

# --------
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]

dn = dict(lista)
print(dn)

dn.popitem()  # Elimina o ultimo item
dn.pop('c2')  # Elimina uma chave
print(dn)
