# Entrada e saída de dados
# input sempre retorna uma string

nome = input('Qual o seu nome')
print(f'O usuário digitou {nome} e o tipo da variável é'
        f'{type (nome)}')

nome2 = input('Digite o seu nome: ')
idade = input('Sua idade: ')

anoNascimento = 2019 - int(idade)
print(f'{nome2} tem {idade} anos e nasceu em {anoNascimento}.', end='\n\n')

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

print(numero1 + numero2)