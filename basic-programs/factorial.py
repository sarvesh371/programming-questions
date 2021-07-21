import math

a = int(input('Enter number to get the factorial: '))

print(math.factorial(a))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return n * factorial(n - 1)

def check_factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

print(factorial(a))
print(check_factorial(a))

