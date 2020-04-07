from time import time, sleep


def velocidade(func):
    def interna(*args, **kwargs):
        startTime = time()
        resultado = func(*args, **kwargs)
        endTime = time()
        tempo = (endTime - startTime) * 1000

        print(f'\nA função {func.__name__} '
              f'levou {tempo:.2f}ms para executar')
        # return resultado
    return interna


@velocidade
def demora():
    for i in range(10):
        print(i, end='')


demora()
