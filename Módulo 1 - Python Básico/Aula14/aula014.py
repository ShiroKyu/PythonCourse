'''

Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - numeros flutuants (float)
:.2f - Casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro

'''

num1 = 10
num2 = 3
divisao = num1 / num2
print(f'{divisao:.2f}')

num3 = 1
print(f'{num3:0>10}')

num4 = 1150
print(f'{num4:9>20}')

nome = 'Paulo Sérgio'
print(len(nome))
print(f'{nome:#^20}')
print('{:*^20}'.format(nome))