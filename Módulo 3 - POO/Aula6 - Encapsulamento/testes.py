class Pokemon:
    def __init__(self, nome, tipo, evolucoes):
        self.nome = nome
        self.tipo = tipo
        self.evolucoes = evolucoes
        self.__mega = False

    def imprimirAtributos(self):
        print(
            f'Nome: {self.nome}\nTipo: {self.tipo}\nEvoluções: {self.evolucoes}\nMega-evolução: {self.__mega}')

    # Usando getters e setters pra ver os atributos privados '__mega' de forma mais fácil
    @property
    def mega(self):
        # Agora pode-se obter o atributo '__mega', usando: pikachu.mega
        return self.__mega

    @mega.setter
    def mega(self, valor):
        if not isinstance(valor, bool):
            return

        self.__mega = valor


pikachu = Pokemon('Pikachu', 'Elétrico', 3)

# Vai dar erro, pois '__mega' é privado
# print(pikachu.__mega)

# Criou-se outro atributo '__mega'
pikachu.__mega = True
print(pikachu.__mega)

# Para imprimir o verdadeiro
print(pikachu._Pokemon__mega)
print()

pikachu.imprimirAtributos()
print()

# Usando o setter pra setar um novo valor
pikachu.mega = True
# Usando getter pra obter o valor
print(pikachu.mega)
