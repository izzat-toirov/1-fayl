import os
os.system("cls")
def func(num, count=2):
    if num <= 1:
        return False
    if count * count > num:
        return True
    if num % count == 0:
        return False
    return func(num, count + 1)

def print_primes(n, current=0):
    if current > n:
        return
    if func(current):
        print(current)
    print_primes(n, current + 1)

n = int(input("N son kiriting: "))
print_primes(n)