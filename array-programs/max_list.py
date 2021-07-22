list1 = [20, 10, 20, 4, 100]
maximum = list1[0]

for i in range(1, len(list1)):
    if list1[i] > maximum:
        maximum = list1[i]
        
print(maximum)
print(max(list1))
