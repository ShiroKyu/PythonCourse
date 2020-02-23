'''
LEN
'''

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Caracteres insuficientes')
else:
    print('Você foi cadastrado no sistema')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite alguma coisa: ')

print(f'A quantidade total de caracteres digitados foi: {len(string1) + len(string2)}')

# len(string2) ===== strin2.__len__()