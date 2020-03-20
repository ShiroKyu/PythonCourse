def lenStr(str):
    if str == '':
        return 0
    return 1 + lenStr(str[1:])


print(lenStr('Hello World'))
