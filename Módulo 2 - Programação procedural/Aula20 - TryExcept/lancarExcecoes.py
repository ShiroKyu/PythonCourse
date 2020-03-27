def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)


x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
