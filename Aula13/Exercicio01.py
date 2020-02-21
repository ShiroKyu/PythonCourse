num = input('Digite um número: ')

try:
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é impar.')
except:
    print('Você não digitou um número.')
