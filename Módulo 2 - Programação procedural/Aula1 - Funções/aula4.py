'''
Escopo de variável
'''

variavel = 'Valor'


def func():
    print(variavel)


def func2():
    # global variavel
    variavel = 'Outro valor'
    print(variavel)

# def func3():
#   print(variavel)
#   variavel = 1234
#  print(variavel)
# erro, tentar acessar uma variavel local antes de atribuir


func()
func2()

print(variavel)
