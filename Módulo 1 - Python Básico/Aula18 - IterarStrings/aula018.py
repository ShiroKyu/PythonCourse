'''
Iterando strings
STRINGS SÃO IMUTAVEIS EM PYTHON
'''

string = 'O rato roeu a roupa do rei de Roma'
print(string[2], end='\n\n')

cont = 0


novaString = ''
while cont < len(string):

    if string[cont] == 'r':
        novaString = novaString + string[cont].upper()
    else:
        novaString = novaString + string[cont]

    cont += 1

print(string, novaString, sep='  =  ')
