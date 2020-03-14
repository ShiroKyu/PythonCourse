from random import choice

moves = ('pedra', 'papel', 'tesoura')
machineMove = choice(moves)

print('Faça a sua jogada: ')
playerMove = int(input('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\nJogada: '))
text = f'A máquina escolheu {machineMove}'

if machineMove == 'pedra':
    if playerMove == 1:
        print(f'{text}. Empate')
    elif playerMove == 2:
        print(f'{text}. Você venceu.')
    else:
        print(f'{text}. Você perdeu.')

elif machineMove == 'papel':
    if playerMove == 1:
        print(f'{text}. Você perdeu.')
    elif playerMove == 2:
        print(f'{text}. Empate.')
    else:
        print(f'{text}. Vocẽ ganhou.')

else:
    if playerMove == 1:
        print(f'{text}. Você ganhou.')
    elif playerMove == 2:
        print(f'{text}. Você perdeu.')
    else:
        print(f'{text}. Empate.')
