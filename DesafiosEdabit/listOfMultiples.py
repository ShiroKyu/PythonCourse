# list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]


def list_of_multiples(num, length):
    lista = []
    n = num

    for x in range(length):
        lista.append(n)
        n += num

    return lista


def list_of_multiples2(num, length):
    return [x * num for x in range(1, length+1)]


print(list_of_multiples2(7, 5))
