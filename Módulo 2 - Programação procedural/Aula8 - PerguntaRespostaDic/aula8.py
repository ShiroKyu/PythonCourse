import random
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {
            'a': 1,
            'b': 4,
            'c': 5
        },
        'respostaCerta': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 X 2 ',
        'respostas': {
            'a': 4,
            'b': 2,
            'c': 6
        },
        'respostaCerta': 'c'
    }
}


respostasCertas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['respostaCerta']:
        print('Você acertou')
        respostasCertas += 1
    else:
        print('Você errou')

    print()

qtdPerguntas = len(perguntas)
porcentagem_acerto = respostasCertas / qtdPerguntas * 100

print(f'Você acertou {respostasCertas} respostas')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
