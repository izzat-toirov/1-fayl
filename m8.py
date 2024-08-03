import os
os.system("cls")

def fun(n):
    return isinstance(n, str)

lst=[True, 'salom', 67, 35, 'nima gap']
a=list(filter(fun, lst))
print(a)