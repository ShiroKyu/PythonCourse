class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, val_assinatura):
        # Chama o construtor de Cliente e por sua vez, Pessoa
        print(super())
        super().__init__(nome, idade)
        self.val_assinatura = val_assinatura

    # Sobrescrevendo o método da classe pai
    def falar(self):
        # executa primeiro o método da classe pai e depois o da filha
        # super().falar()

        # executa o método de uma classe especifica
        Pessoa.falar(self)
        print('kk eae men')

    def listar(self):
        print(f'{self.nome}/{self.idade}/{self.val_assinatura}')
