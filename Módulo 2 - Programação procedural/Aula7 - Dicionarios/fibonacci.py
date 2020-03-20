fibCache = {}


def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    elif n in fibCache:
        return fibCache[n]

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(500))
