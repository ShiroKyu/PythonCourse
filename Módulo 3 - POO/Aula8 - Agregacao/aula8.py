# Uma classe depende da outra pra funcionar CORRETAMENTE

from classes import Carrinho_de_Compras, Produto

carrinho = Carrinho_de_Compras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', '10000')
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produtos()
