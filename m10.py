import os
os.system("cls")

def func(n):
    if isinstance(n, int):
        return float(n)
    else:
        return int(n)
    
lst=[4, 5.6, 6, 7.8, 1, 6,8.9]
a=list(map(func, lst))
print(a)