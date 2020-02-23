num = 10

while num >= 0:
    print(num)
    num -= 1

while num <= 10:
    print(num)
    num += 1
    if num == 5:
        break

while True:
    num2 = input('Digite um número: ')
    num3 = input('Digite outro número: ')

    if not num2.isnumeric() or not num3.isnumeric():
        print('Você precisa digitar um número: ')
        continue
