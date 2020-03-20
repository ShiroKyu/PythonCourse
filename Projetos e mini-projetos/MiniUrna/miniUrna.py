candidatos = {}
parada = 2

while parada == 2:
    nome = input('Informe o nome do candidato: ')
    partido = int(input('Informe o número: '))
    sigla = input('Informe a sigla: ')
    candidatos[nome] = {}
    candidatos[nome]['partido'] = partido
    candidatos[nome]['sigla'] = sigla
    candidatos[nome]['votos'] = 0
    print('Deseja parar de inserir? ')
    parada = int(input('[1] Sim, [2] - Não\nEscolha: '))

qtd = len(candidatos)
