from math import pow

nome = 'Paulo'
idade = 32
altura = 1.80
eMaior = idade > 18
peso = 80

print(nome)
print(idade)
print(altura)
print(eMaior, end='\n\n')

print('O IMC de {} é {}'.format(nome, peso / (altura ** 2)), end='\n\n')
print(type("""40"""))
