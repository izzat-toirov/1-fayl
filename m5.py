import os
os.system("cls")

def func(n, lst1):
    a=n ** 3
    return lst1 > a
    
lst1=[24 ,16, 82, 100, 30, 60]
n=int(input("N son kiriting: "))
a=list(filter(lambda lst1: func(n, lst1), lst1))
print(a)