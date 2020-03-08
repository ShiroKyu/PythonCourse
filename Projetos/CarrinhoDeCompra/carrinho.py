print('--- Carrinho de compras ---', end='\n\n')

carrinho = {}


def comprar(carrinho):
    choise = ''
    while choise != 'n':
        produto = input('Informe o nome do produto: ')
        preco = float(input('Informe o preço do produto: '))
        qtd = int(input('Informe a quantidade que deseja comprar: '))

        carrinho[produto] = {}
        carrinho[produto]['preco'] = preco
        carrinho[produto]['qtd'] = qtd

        choise = input(('Deseja continuar comprando?\n[s] ou [n]\n'))
    return carrinho


def imprimirCarrinho(carrinho):
    for produto, att in carrinho.items():
        print(f'{produto}:')
        for att1, att2 in att.items():
            print(f'\t{att1}: {att2}')


comprar(carrinho)
imprimirCarrinho(carrinho)

'''
while choise != 1 or choise != 2
choise = int(
    input('Deseja pagar a vista ou a prazo:\n[1] - a vista ou [2] - a prazo'))
'''
