class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando')

# Herda Pessoa


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

# Herda Pessoa


class Aluno(Pessoa):
    def estudando(self):
        print(f'{self.nomeclasse} estudando...')
