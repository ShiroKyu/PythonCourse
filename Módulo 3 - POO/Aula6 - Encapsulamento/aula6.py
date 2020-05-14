'''
Public, protected, private
'''

'''
Convenções

_  -> 'Private'/'Protected', não se deve acessar (public_) 
__ -> 'Privado', não deve-se acessar de jeito nenhum (_NOMECLASSE__nomeatributo)

'''

# Público, acessível dentro e fora da classe


class BaseDeDados:

    # Getters e setter podem facilitar na hora de acessar e modificar atributos privados
    @property
    def dados(self):
        return self.__dados

    @dados.setter
    def dados(self, valor):
        self.__dados = valor
    def __init__(self):
        self.__dados = {}

    ########################################

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        if self.__dados:
            for id, nome in self.__dados['clientes'].items():
                print(id, nome)
        else:
            print('Banco de dados vazio.')

    def apaga_cliente(self):
        del self.__dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Paulo')

# Não modificou o atributo privado __dados, apenas criou-se outro
bd.__dados = 'Outra coisa'
# Printa o novo atributo criado na linha de cima
print(bd.__dados)
# Printa o verdadeiro atributo __dados
print(bd._BaseDeDados__dados)
