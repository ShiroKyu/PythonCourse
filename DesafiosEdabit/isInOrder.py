'''
is_in_order("abc") ➞ True

is_in_order("edabit") ➞ False

is_in_order("123") ➞ True

is_in_order("xyzz") ➞ True

'''


def is_in_order(str): return str == ''.join(sorted(str))


print(is_in_order('xyzz'))
