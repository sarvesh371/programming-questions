list1 = [1, 2, 3, 4, 5, 6, 7]

shift_index = 2
temp_list = []
for i in range(0, len(list1)):
    if i > shift_index:
        break
    else:
        temp_list.append(list1[i])

print(list1[shift_index + 1:len(list1)] + temp_list)

print(list1[shift_index + 1:len(list1)] + list1[0:shift_index + 1])
