'''
Count the amount of ones in the binary representation of an integer. 
So for example, since 12 is '1100' in binary, the return value should be 2.

'''


# def count_ones(num):
#     nBin = bin(num)[2:]
#     cont = 0
#     for i in nBin:
#         if i in '1':
#             cont += 1
#     return cont


# Escrevendo algo melhor ...
def count_ones(num):
    return bin(num).count('1')

# Ou em formato lambda

# count_ones2 = lambda num: bin(num).count('1')


print(count_ones(999))
# print(count_ones2(999))
