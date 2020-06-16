class taErradoError(Exception):
    pass


def testar():
    raise taErradoError('Errado')


try:
    testar()
except taErradoError as e:
    print(f'Erro: {e}')
