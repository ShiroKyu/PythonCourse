class A:
    var_classe = 123


a1 = A()
a2 = A()

print(a1.var_classe)
print(a2.var_classe)

A.var_classe = 321

print(a1.var_classe)
print(a2.var_classe)
