string = '0123456789012345678901234567890123456789'
n = 10

lista = [string[i: n + i] for i in range(0, len(string), n)]
print(lista)

retorno = '.'.join(lista)
print(retorno)
