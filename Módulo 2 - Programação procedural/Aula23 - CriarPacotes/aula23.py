#import vendas.calcPreco
#from vendas import calcPreco
from vendas.calcPreco import aumento, reducao

#preco = vendas.calcPreco.aumento(49.90, 15)
preco = aumento(49.90, 15, True)

print(preco)
