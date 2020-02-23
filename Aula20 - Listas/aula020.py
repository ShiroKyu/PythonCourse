# Listas

'''
append, insert, pop, del, clear, extend
append -> adiciona um elemento
insert -> adiciona um elemento em uma posição
pop -> retira da ultima posição
del -> deleta das posições especificadas
extend -> extende uma lista com outra
'''

#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#  -      5    4    3    2    1

# print(lista[::-1]) //Imprime ao contrário

l1 = [1, 2, 3]
l2 = [4, 5, 6]
# l3 = l1 + l2
l1.extend(l2)
print(l1)

l2.append('A')
print(l2)

l2.insert(0, 'Banana')
print(l2)

l2.pop()
print(l2)

del(l2[-1:])
print(l2)

# Exemplo, gerar números de 0 a 100, multiplos de 5
l3 = list(range(0, 101, 5))
print(l3)

l4 = ['String', True, 10, 25.75]
for valor in l4:
    print(f'O valor {valor} é do tipo {type(valor)}')

secreto = 'perfume'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)
    if letra in secreto:
        print('A letra existe na palavra')
    else:
        print('A letra não existe na palavra secreta')
        digitadas.pop()
