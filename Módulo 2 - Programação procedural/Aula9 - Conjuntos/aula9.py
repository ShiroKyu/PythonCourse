'''
- add (adiciona), update (atualiza), clear, discard
- union | (une)
- intersection & (todos os elementos presentes nos dois sets)
- difference - (elementos apenas no set da esquerda)
- symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos   )

'''

s1 = {1, 2, 3, 4, 5}
print(type(s1))

s2 = {}  # Dicionario
s2 = set()

# Algumas operações
s2.add(1)
s2.add((10, 20, 30))
s2.discard((10, 20, 30))
print(s2)
s2.update('Python')
print(s2)
print()

# União
s3 = {1, 2, 3}
s4 = {4, 5, 6}
s5 = s3 | s4
print(s5)

# Intersecção
s6 = {10, 20, 30, 40}
s7 = {10, 20, 50, 70}
s8 = s6 & s7
print(s8)

# Difference
s9 = s7 - s8
print(s9)

# Simmetric difference
s10 = s6 ^ s7
print(s10)


s11 = ['Luiz', 'Paulo', 'Maria']
s12 = ['Luiz', 'Paulo', 'Paulo', 'Maria', 'Luiz']
print(s11 == s12)
s11 = set(s11)
s12 = set(s12)
# Agora, as duas listas(conjuntos), são iguais
print(s11 == s12)
