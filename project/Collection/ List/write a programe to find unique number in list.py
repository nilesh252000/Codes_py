numbers = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 5, 9]
count_dict = {}
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
unique_numbers = []
for num in count_dict:
    if count_dict[num] == 1:
        unique_numbers.append(num)
print("Unique numbers:")
for num in unique_numbers:
    print(num)
