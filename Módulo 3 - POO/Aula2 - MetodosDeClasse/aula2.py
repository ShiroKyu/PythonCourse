# Métodos de classe X Métodos de instância


class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Fábrica o objeto
    @classmethod
    def por_ano_nascimento(cls, nome, anoNascimento):
        idade = cls.ano_atual - anoNascimento
        return cls(nome, idade)


# p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)

print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
