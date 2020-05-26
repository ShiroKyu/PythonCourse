from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')

cliente2 = Cliente('Maria', 20)
cliente2.insere_endereco('Salvador', 'Ba')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')

cliente3 = Cliente('Paulo', 18)
cliente3.insere_endereco('São paulo', 'SP')

#del Cliente


clienteN = Cliente('Cliente aleatório', 99)
clienteN.insere_endereco('Amazonas', 'AM')

# cliente1.lista_enderecos()
cliente2.lista_enderecos()
cliente3.lista_enderecos()
