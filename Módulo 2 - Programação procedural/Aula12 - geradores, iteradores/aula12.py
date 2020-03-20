import sys
import time

lista = [0, 1, 2, 3, 4]

print(hasattr(lista, '__iter__'))  # é iteravel

print(hasattr(lista, '__next__'))

lista = iter(lista)
print(hasattr(lista, '__next__'))  # transformou em um iterador

lista2 = list(range(10))
print(sys.getsizeof(lista2))


def gera():
    r = []
    for n in range(100):
        yield n          # entrega o valor e para a execução, quando for chamado denovo retoma a execução
        time.sleep(0.1)


# for v in gera():
#    print(v)

g = gera()
for n in g:
    print(n)

lista3 = [x for x in range(100)]  # lista
lista4 = (x for x in range(100))  # gerador, forma rapida de fazer um
print(type(lista3), type(lista4))
