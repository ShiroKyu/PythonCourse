# Métodos de classe X Métodos de instância
from random import randint


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

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


#p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)

print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())


print('\n', '#' * 20, '\n')


class Aluno:

    alunos_cadastrados = 0

    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def imprimeAluno(self):
        print(self.nome, self.idade, self.curso)

    @classmethod
    def criar_aluno(cls, nome, idade, curso):
        cls.alunos_cadastrados += 1
        return cls(nome, idade, curso)

    @classmethod
    def imprime_qtd_cadast(cls):
        print(cls.alunos_cadastrados)

    # def imprime_qtd_cadast(self):
    #     print(self.alunos_cadastrados)


#aluno = Aluno('Paulo', 18, 'ADS')
aluno1 = Aluno.criar_aluno('Paulo', 19, 'ADS')
aluno1.imprimeAluno()
aluno1.imprime_qtd_cadast()


aluno2 = Aluno.criar_aluno('Joao', 12, "ENG")
aluno2.imprime_qtd_cadast()
aluno1.imprime_qtd_cadast()
