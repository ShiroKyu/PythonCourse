def readjust(valor, percentual):
    return (valor * percentual / 100) + valor


newVal = readjust(15, 100)
print(newVal)
