def dobra(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


PI = 3.1415

print('Isso vem primeiro ao importar o módulo')
print(__name__)


# Se o módulo tiver sendo chamado por outro arquivo, o __name__ se tornará o nome do módulo.
# Caso contrário, será __main__
# __name__ é uma váriavel que indica o nome do módulo atual

if __name__ == '__main__':
    print('Isso não será executado ao importar')
