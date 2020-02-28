'''
Funções - def
'''


def funcao():
    print('Hello World')


funcao()


def outraFuncao(msg='Olá', nome='Indefinido'):
    print(msg + ' ' + nome)


outraFuncao()
outraFuncao('Bom dia')
outraFuncao('Boa noite', 'Paulo')
outraFuncao(nome='Luiz', msg='Até mais')


def media(nota1, nota2):
    return (nota1 + nota2) / 2


media1 = media(8.5, 10)
print(media1)
