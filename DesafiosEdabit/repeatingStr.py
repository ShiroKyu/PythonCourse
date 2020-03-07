def double_char(txt):
    result = ''
    for letter in txt:
        result += letter * 2
    return result


print(double_char('Paul'))

dic = [
    {'nome': 'Paulo', 'idade': 18},
    {'nome': 'João', 'idade': 15}
]

dic.sort(key=lambda item: item['idade'], reverse=False)
print(dic)
