import os
os.system("cls")

def func(n):
    return isinstance(n, int)

lst=[3 ,5.6, 7.1, 6.2, 8]
a=list(filter(func, lst))
print(a)