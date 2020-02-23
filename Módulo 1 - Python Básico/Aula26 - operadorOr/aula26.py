nome = input('Qual o seu nome: ')

'''
if nome:
    print(nome)
else:
    print('Não digitou nada')
'''

print(nome or 'Não digitou nada')

a = 0
b = None
c = False
d = []
e = {}
f = 10
g = 'Paulo'
var = a or b or c or d or e or f or g
print(var)
