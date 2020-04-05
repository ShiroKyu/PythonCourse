# Sempre considerar a importação do arquivo __main__, no caso, o 'aula23.py' que é o arquivo principal
from vendas.formata.formataPreco import real


def aumento(valor, porcentagem, format=False):
    r = valor + (valor * porcentagem / 100)

    if format:
        return real(r)
    else:
        return r


def reducao(valor, porcentagem, format=False):
    r = valor - (valor * porcentagem / 100)

    if format:
        return real(r)
    else:
        return r
