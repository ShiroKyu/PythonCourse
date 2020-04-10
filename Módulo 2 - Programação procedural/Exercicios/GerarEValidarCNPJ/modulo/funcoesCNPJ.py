from re import sub


def formatar(cnpj): return sub(r'[^0-9]', '', cnpj)


def calcPrimeiroDigito(cnpj):
    contagem = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

    # Faz os produtos e faz a somatória
    digito = sum([x * y for x, y in zip(cnpj, contagem)])
    digito = 11 - (digito % 11)
    return 0 if digito > 9 else digito


def calcSecDigito(cnpj):
    contagem = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

    # Faz os produtos e faz a somatória
    digito = sum([x * y for x, y in zip(cnpj, contagem)])
    digito = 11 - (digito % 11)

    return 0 if digito > 9 else digito


def verificar(cnpj):

    cnpjOriginal = formatar(cnpj)

    # Converter as strings em inteiros
    novoCnpj = [int(x) for x in cnpjOriginal]
    novoCnpj.pop()
    novoCnpj.pop()

    # Calcular o primeiro digito
    primDigito = calcPrimeiroDigito(novoCnpj)

    # Calcular o segundo digito
    novoCnpj.append(primDigito)
    secDigito = calcSecDigito(novoCnpj)

    # Juntar os digitos com o cnpj
    novoCnpj.append(secDigito)
    novoCnpj = [str(x) for x in novoCnpj]

    novoCnpj = ''.join(novoCnpj)

    # Verificar se é valido
    if cnpjOriginal == novoCnpj:
        return True
    return False
