variavel = ['Luiz', 'Paulo', 'Maria', 'João']

for valor in variavel:
    if valor.lower().startswith('p'):
        print('Valor encontrado')
        print(valor)
        continue

# Se o for terminar, executa o else,
else:
    print('Não existe palavra com P')
