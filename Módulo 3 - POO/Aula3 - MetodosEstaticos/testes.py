import numpy as np


class Pokemon:

    def __init__(self, nome, tipo, nivel):
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel

    # Não mexe com o objeto ou a classe em si
    @staticmethod
    def lista_todos_tipos():
        tipos = np.array(['Fogo', 'Água', 'Elétrico', 'Terra', 'Voador'])

        for tipo in tipos:
            print(tipo)

    @classmethod
    def adiciona_pokemon_por_id(cls, nome, tipo, nivel, id):
        cls.nome = nome
        cls.tipo = tipo
        cls.nivel = nivel
        cls.id = id
        return cls(nome, tipo, nivel)


#pkm1 = Pokemon('Pikachu', 'Elétrico', 25)
# pkm1.lista_todos_tipos()
pkm1 = Pokemon.adiciona_pokemon_por_id('Pikachu', 'Elétrico', 25, '001')
print(pkm1.id)
