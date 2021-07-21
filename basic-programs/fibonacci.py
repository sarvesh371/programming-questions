num = int(input('Enter the length of series: '))

a = 0
b = 1
series = []

for i in range(0, num):
    c = a + b
    series.append(a)
    a = b 
    b = c

print(series)
