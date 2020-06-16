class A:
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        # toda classe de python deriva da classe object
        # nesse caso, super() == object
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print(args)
        print(*kwargs)

    def __init__(self):
        print('Eu sou init')


a = A()
b = A()
c = A()
a(1, 2, 3, 4, 5, nome='Luiz')
