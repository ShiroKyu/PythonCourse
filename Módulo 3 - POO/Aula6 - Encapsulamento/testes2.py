class Pokemon:
    def __init__(self, nome, tipo, nivel, apelido=None):
        self.nome = nome
        self.apelido = apelido
        self.__tipo = tipo
        self.__nivel = nivel

    def listar1(self):
        print(
            f'{self.nome}, {self.apelido or "Sem apelido"}, {self.__tipo}, {self.__nivel}')

    # Getters e setters
    @property
    def tipo(self):
        return self.__tipo

    @property
    def nivel(self):
        return self.__nivel


pkm1 = Pokemon('Pikachu', 'Elétrico', '36')
pkm1.listar1()

# Método não muito bom de acessar um atributo privado
# print(pkm1._Pokemon__tipo)

print(pkm1.nivel, pkm1.tipo)
