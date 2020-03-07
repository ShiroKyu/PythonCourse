def func1(func2, *args, **kwargs):
    return func2(*args, **kwargs)


def func2(nome):
    return f'Oi {nome}'


def func3(nome, saudacao):
    return f'{saudacao} {nome}'


executando = func1(func2, 'Luiz')
print(executando)
