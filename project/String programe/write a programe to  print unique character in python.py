input_string = "yaadccdekp"
count_dict = {}
for char in input_string:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
unique_characters = []
for char in count_dict:
    if count_dict[char] == 1:
        unique_characters.append(char)
print("Unique characters:")
for char in unique_characters:
    print(char)
