# Classe genérica que não quero instanciar

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando... B')


# Não da pra instanciar B sem ter o método 'falar' de A
a = B()
a.falar()
