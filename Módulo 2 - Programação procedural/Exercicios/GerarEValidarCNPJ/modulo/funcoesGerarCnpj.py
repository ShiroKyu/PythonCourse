'''

04.252.011/0001-10

'''

from random import randint
from modulo.funcoesCNPJ import calcPrimeiroDigito, calcSecDigito


def formatarCNPJ(cnpj):
    cnpj.insert(2, '.')
    cnpj.insert(6, '.')
    cnpj.insert(10, '/')
    cnpj.insert(15, '-')
    return ''.join(cnpj)


def geradorCNPJ():

    primDigito = str(randint(0, 9))
    secDigito = str(randint(0, 9))

    secBloco = str(randint(100, 999))
    tercBloco = str(randint(100, 999))
    quartBloco = '0001'

    cnpj = primDigito + secDigito + secBloco + tercBloco + quartBloco
    cnpj = [int(x) for x in cnpj]

    penDigito = calcPrimeiroDigito(cnpj)
    cnpj.append(penDigito)
    ultDigito = calcSecDigito(cnpj)
    cnpj.append(ultDigito)

    cnpj = [str(x) for x in cnpj]
    cnpj = formatarCNPJ(cnpj)

    return cnpj
