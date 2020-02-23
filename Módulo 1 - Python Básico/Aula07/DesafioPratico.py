nome = 'Paulo'
idade = 18
altura = 1.62
peso = 50
anoAtual = 2020
anoNascimento = anoAtual - idade - 1
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}KG', end='\n')
print(f'O IMC de {nome} é {imc:.2f}', end='\n')
print(f'{nome} nasceu em {anoNascimento}')

print("Meu nome é 'Luiz Otávio', mas me chamam de 'Otávio Miranda'", end='\n\n')

# Pode concatenar strings, mas não um Int e uma Str por exemplo
var1 = 'a'
var2 = 'b'
print(f'{var1 + var2}')