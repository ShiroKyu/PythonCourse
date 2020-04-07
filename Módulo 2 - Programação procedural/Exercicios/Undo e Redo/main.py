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

toDo = []
reDo = []
lastTask = ''


def adicionar(task):
    toDo.append(task)


def listar(toDo):
    if not toDo:
        print('Nada a imprimir')
        return
    for task in toDo:
        print(task)


def unDo(toDo):
    pass


def reDo(toDo):
    pass


while True:
    print('##### Agenda de tarefas #####\n')
    print('[1] - adicionar\n[2] - listar\n[3] - Desfazer\n[4] - Refazer')
    opc = int(input('Informe uma opção: '))

    # if opc == 1:
    #     task = input('Informe a tarefa: ')
    #     adicionar(task)
    #     reDo.append(task)
    #     continue

    # elif opc == 2:
    #     listar(toDo)
    #     continue

    # elif opc == 3:
    #     unDo(toDo)

    # elif opc == 4:
