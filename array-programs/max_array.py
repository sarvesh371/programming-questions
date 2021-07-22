arr = [20, 10, 20, 4, 100]
maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
        
print(maximum)
print(max(arr))
