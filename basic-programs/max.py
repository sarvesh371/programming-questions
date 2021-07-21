a = input('Enter first number: ')
b = input('Enter Second number: ')

def check_max(a, b):
    if a >= b:
        return a
    else:
        return b

print(check_max(a, b))

print(max(a, b))
