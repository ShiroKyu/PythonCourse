import json
import os
file = open('abc.txt', 'w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0, 0)  # Volta o cursor pro começo
print('Lendo linhas')
print(file.read())
print('########')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#########')

file.seek(0, 0)
# print(file.readlines())

for linha in file.readlines():
    print(linha, end='')

file.close()


print('#' * 30)

try:
    file = open('efg.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()


with open('hij.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print(file.read())

with open('hij.txt', 'a+') as file:
    file.write('Outra linha')
    file.seek(0)
    print(file.read())


os.remove('hij.txt')

print('#################')


d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25
    },
    'Pessoa 2': {
        'nome': 'Paulo',
        'idade': 19
    }
}

d1_json = json.dumps(d1, indent=True)

with open('d1.json', 'w+') as file:
    file.write(d1_json)
