my_list = [1, 2, 3, 4, 5]
reversed_list = []

# Iterate through the original list in reverse order
for i in range(len(my_list) - 1, -1, -1):
  reversed_list.append(my_list[i])

# Print the original and reversed lists
print("Original list:", my_list)
print("Reversed list:", reversed_list)