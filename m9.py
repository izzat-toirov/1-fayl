import os
os.system("cls")

def func(n):
    return not n % 2
    
lst=[3, 4, 8, 24 ,67, 80, 88]
a=list(filter(func, lst))
print(a)