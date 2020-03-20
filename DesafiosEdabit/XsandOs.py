'''
Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

Return a boolean value (True or False).
The string can contain any character.
When no x and no o are in the string, return True.

'''


def XO(txt):
    x, o = 0, 0
    for i in txt:
        if i.lower() == 'x':
            x += 1
        elif i.lower() == 'o':
            o += 1
    if x == o:
        return True
    return False


print(XO('ooxx'))


def XO2(text):
    return text.lower().count('x') == text.lower().count('o')
