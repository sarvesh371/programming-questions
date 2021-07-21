a = int(input('Enter the number: '))

def armstrong(n):
    
    order = len(str(n))
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        print(digit)
        sum += digit ** order
        temp //= 10
        print(temp)

    if sum == n:
        return True
    else:
        return False

print(armstrong(a))

