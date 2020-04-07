def master(funcao):
    def slave():
        print('Agora estou decorada')
        funcao()
    return slave


@master
def falaOi():
    print('Oi')


falaOi()
