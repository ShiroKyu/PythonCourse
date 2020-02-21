'''
IF, ELIF, ELSE
'''

num1 = 10
num2 = 5
num3 = 2

if num1 > 20:
    print(num1)
elif num1 >= 10:
    print(num1 + num1, end='\n\n')
else:
    print('Condições falsas')

'''
OPERADORES RELACIONAIS
== > >= < <= !=
'''

print(2 == 2)

nome1 = 'Paulo'
nome2 = 'João'
print(nome1 == nome2)

n1 = 2
n2 = '2'
print(n1 == n2)

if 2 >= '2':
    print('Certo')
else:
    print('erro')