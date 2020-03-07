'''
Tuplas

Diferença entre listas e tuplas - Tuplas são imutáveis
-> Não se pode adicionar, remover ou alterar seus valores
'''
t1 = (1, 2, 3, 'Luiz', 'Paulo', True)
t2 = 1, 2, 3, 'Luiz'
t3 = 1,  # Tupla de 1 elemento só

for valor in t2:
    print(valor)

t4 = t1 + t2  # Concatenação
print(t4)

t4 *= 5  # Multiplicar tupla
print(t4)

# Modificar valores da tupla (transformando em lista)
t2 = list(t2)
t2[0] = 'Novo item'
t2 = tuple(t2)
print(t2)
