'''
Função range (start=0; stop, step=1)
'''

# for n in range(20, 10, -1): ///Imprime os números de 20 a 11
for n in range(1, 11):
    if n % 2 == 0:
        print('Numero par')
    else:
        print(n)

string = 'Paulo'
novaString = ''

for letra in string:
    print(letra)
    novaString += letra


print(string, novaString)
