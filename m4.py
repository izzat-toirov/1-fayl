import os
os.system("cls")

def func(n):
    if  n > 0:
        return -1 * n
    else:
        return n * 2
    
lst=[4, -6, 7, -2, 5, -10]
lst=list(map(func, lst))
print(lst)