def fizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'

    return num


var = fizzBuzz(8)
print(var)


for i in range(101):
    var = fizzBuzz(i)
    print(var)
