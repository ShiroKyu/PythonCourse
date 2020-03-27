try:
    a = []
    print(a[0])
except NameError as erro:
    print(erro)

except (IndexError, KeyError) as erro:
    print('erro de indice ou chave')
except Exception as erro:
    print(erro)

else:
    print('oo')

finally:
    print('Terminado')

print(a)
