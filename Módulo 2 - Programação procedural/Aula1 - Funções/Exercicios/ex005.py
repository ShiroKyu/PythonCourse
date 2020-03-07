def func1(func2):
    return func2()


def func2():
    return 'Olá'


var = func1(func2)
print(var)
