from datetime import datetime


class Pessoa:

    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.falando} já esta falando')
            return

        print(f'{self.nome} está falando')
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def getAnoNascimento(self):
        return self.anoAtual - self.idade
