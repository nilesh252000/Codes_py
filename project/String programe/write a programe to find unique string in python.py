numbers = ["yogesh","yogesh","nilesh","raju","raju"]
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

# Output the unique numbers
print("Unique numbers:")
for num in unique_numbers:
    print(num)
