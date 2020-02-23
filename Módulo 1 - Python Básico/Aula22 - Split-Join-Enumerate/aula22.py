'''
Split, Join, enumerate

* Split - Dividir uma string
* Join  - Juntar uma lista
* Enumerate - enumerar elementos da lista iteráveis
* strip - remove espaços do inicio e fim
'''

string = 'o Brasil é o pais do futebol, e penta'
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista1:
    print(f'O valor {valor} apareceu {lista1.count(valor)} vez')

lista3 = ['O', 'Brasil', 'joga', 'hoje']
lista3 = '-'.join(lista3)
print(lista3)

lista4 = ['Eu', 'adoro', 'programar']

for indice, valor in enumerate(lista4):
    print(indice, valor)

lista5 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for valor1, valor2, valor3 in lista5:
    print(valor1, valor2, valor3)
