"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""

from modulos.funcoes import adicionar, listar, desfazer, refazer

if __name__ == "__main__":
    toDo = []
    reDo = []

    while True:

        print('##### Agenda de tarefas #####\n')
        print(
            '[1] - adicionar\n[2] - listar\n[3] - Desfazer\n[4] - Refazer\n[5] - Sair\n')
        opc = int(input('Informe uma opção: '))

        if opc == 1:
            task = input('Informe a tarefa: ')
            adicionar(toDo, task)
            continue

        elif opc == 2:
            listar(toDo)
            continue

        elif opc == 3:
            desfazer(toDo, reDo)
            continue

        elif opc == 4:
            refazer(toDo, reDo)
            continue

        elif opc == 5:
            break
