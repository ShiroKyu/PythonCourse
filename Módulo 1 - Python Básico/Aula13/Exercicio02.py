hora = input('Informe as horas (0 a 23): ')

try:

    if hora >= 0 or hora <= 23:
        hora = int(hora)
        if hora >= 0 and hora <= 11:
            print('Bom dia.')
        elif hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
    else:
        print('Horário inválido.')

except:
    print('Hora inválida.')
