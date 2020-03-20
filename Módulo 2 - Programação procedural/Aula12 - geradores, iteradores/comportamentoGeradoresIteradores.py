# lists, tuples, str -> sequences -> iterável
# next() -> retorna o proximo item de um iterador

nome = 'Luiz Otavio'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))  # L
print(next(gerador))  # U
print(next(gerador))  # I
print(next(gerador))  # Z

for l in gerador:  # Consumiu o restante das letras, O T A V I O
    print(l)

print('#' * 80)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))

except:
    pass

print('Cade os valores?')
for v in iterador:  # Os valores do iterador ja foram consumidos
    print(valor)

'''
for letra in nome:  # For converte 'nome' em iterador em tempo de execução
    print(letra)
print('#' * 80)

for letra in nome:
    print(letra)
'''
