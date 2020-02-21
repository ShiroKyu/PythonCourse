'''

AULA DE FATIAMENTO DE STRINGS

'''


# positivos [0, 1, 2, 3]
# negativos[0, 1, 2, 3]
texto = 'Python s2'

novo_texto = texto[0::2]  # vai até o final pulando de 2 em dois
# [:6], [7:] -> começa do 7 e vai até o final
# texto[:-3] imprime do contrário a partir do -3

try:
    print(f'{novo_texto}')
except:
    print('Indíce não existe.')
