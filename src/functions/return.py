from functools import reduce
from operator import mul
def func():
    pass # null statement
    #print("ABC")
print(func())

def factorial(n):
    print("="*10, "Factorial", "="*10)
    fact = n
    for num in range(1,n):
        fact = fact*num
    return fact

print(factorial(10))
print(factorial(5))

def factorial(n):
    return reduce(mul, range(1,n+1), 1)


print(factorial(10))
print(factorial(5))

print("="*10, "Recursive Factorial","="*10 )
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

print(factorial(10))
print(factorial(5))

def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))
print(get_multiples_of_five(50))