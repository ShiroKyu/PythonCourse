def adicionar(toDo, task):
    toDo.append(task)
    print()


def listar(toDo):
    print()
    if not toDo:
        print('Nada a imprimir')
        return

    print('Tarefas: ')
    for task in enumerate(toDo):
        print(task)

    print()


def desfazer(toDo, reDo):
    if not toDo:
        print('Nada a desfazer')

    last = toDo.pop()
    reDo.append(last)

    print()


def refazer(toDo, reDo):
    if not reDo:
        print('Nada a refazer')
        return

    task = reDo.pop()
    toDo.append(task)

    print()
