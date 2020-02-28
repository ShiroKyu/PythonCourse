def funcao(var):
    print(var)


variavel = funcao('Valor que eu quero')
print(variavel)

if variavel:
    print(variavel)
else:
    print('Nenhum valor')


def f(var):
    print(var)


def dumb():
    return f


var = dumb()
var('olá')
