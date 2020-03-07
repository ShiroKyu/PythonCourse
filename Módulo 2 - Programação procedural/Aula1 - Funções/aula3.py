def func(a1, a2, a3, a4, a5, nome=None):
    print(a1, a2, a3, a4, a5, nome)


func(1, 2, 3, 4, 5, 'Paulo')


def outraFunc(*args, **kwargs):
    print(f'Args: {args}')      # args -> tupla de parametros
    # kwargs -> argumentos nomeados, dicionario de parametros
    print(f'Kwargs: {kwargs}')
    for i in kwargs:
        print(kwargs[i])


outraFunc(1, 2, 3, nome='Paulo', sobrenome='Sérgio')


def teste(*args):
    soma = 0

    for num in args:
        soma += num
    return soma


var = teste(1, 2, 3, 4, 5)
print(var)

# OBS: Tupla: (1, 2, 3), lista: [1, 2, 3], dicionario: {n1: 1, n2: 2, n3: 3}
