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

acertos = 0

for pk, pr in perguntas.items():
    print(f'{pk}: {pr["pergunta"]}')
    for alt, resp in pr["respostas"].items():
        print(f'{alt}: {resp}')

    resposta = input('Sua resposta: ')
    if resposta == pr["respostaCerta"]:
        acertos += 1

print(acertos)
