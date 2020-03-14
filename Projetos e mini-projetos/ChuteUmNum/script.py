from random import randint

print('---- Jogo da adivinhação ----', end='\n\n')
print('Regras: \n[1] Informe até que número você deseja adivinhar\nEx: adivinhar números de 0 até 100, digite 100', end='\n\n')

num = int(input('Informe até que número deseja gerar: '))
num = randint(0, num)
escolha = 0

while escolha != num:
    escolha = int(input('Faça um chute: '))
    if escolha == num:
        print('Parabéns, acertou o número.')
        break
    else:
        print('Desculpe, você errou.')
