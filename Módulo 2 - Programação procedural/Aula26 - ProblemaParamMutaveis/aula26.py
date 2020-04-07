def listaDeClientes(clienteIteraveis, lista=[]):
    lista.extend(clienteIteraveis)
    return lista


# Ambos recebem o endereço de memória de 'lista', por isso são iguais. Alterar uma, modifica a outra
# Ao chamar a função uma vez, o parâmetro padrão passa a ser '['João', 'Maria', 'Eduardo']'
clientes1 = listaDeClientes(['João', 'Maria', 'Eduardo'])

# Ao chamar a segunda vez, junta-se ao parâmetro padrão
clientes2 = listaDeClientes(['Marcos', 'Jane', 'Paul'])


print(clientes1)
print(clientes2)
