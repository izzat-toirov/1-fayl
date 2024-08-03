import os
os.system("cls")

def func(n):
    a=list(map(bool, n))
    return a

lst=[1, 0, 1, 0, 1, 1, 0]
print(func(lst))