class Pokemon:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def atacar(self):
        print('Atacando')

    def listar(self):
        print(self.nome, self.tipo)


class MegaPokemon(Pokemon):
    def __init__(self, nome, tipo, lv):
        super().__init__(nome, tipo)
        # Privado
        self.__lv = lv

    def listar(self):
        super().listar()
        # Correspondente a pkm1._MegaPokemon__lv
        print(self.__lv)


pkm1 = MegaPokemon('Delphox', 'Fire', 36)
pkm1.listar()
