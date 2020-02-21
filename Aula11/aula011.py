num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

#isnumeric isdigit isdecimal

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)

except:
    print('error')
