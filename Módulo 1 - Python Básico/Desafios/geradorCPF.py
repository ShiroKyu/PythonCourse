from random import randint

numAleatorio = str(randint(100000000, 999999999))
novoCpf = numAleatorio

soma = 0
validacao1 = 10
validacao2 = 11

# Validar o digito 1
for digito in novoCpf:
    soma += (int(digito) * validacao1)
    validacao1 -= 1

formula = 11 - (soma % 11)
# se o resultado for maior que 9, então é 0
digito1 = formula if (formula <= 9) else 0
novoCpf += str(digito1)

# Validar o digito 2
soma = 0
for digito in novoCpf:
    soma += (int(digito) * validacao2)
    validacao2 -= 1

formula = 11 - (soma % 11)
digito2 = formula if (formula <= 9) else 0
novoCpf += str(digito2)

print(novoCpf)
