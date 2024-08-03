import os
import math
os.system("cls")

def rekursiv(n):
    a=list(map(math.ceil, n))
    return a

lst=[2, 3, 5.5, 6.7 ,8]
print(rekursiv(lst))