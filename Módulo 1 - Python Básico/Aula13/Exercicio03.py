nome = input('Informe o seu primeiro nome: ')

try:
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif len(nome) <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é maior que o normal.')

except:
    print('Nome inválido.')