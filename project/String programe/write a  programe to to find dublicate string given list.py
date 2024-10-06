str_list = ["Nilesh", "Nilesh", "jamir"]

# Initialize a set to track seen elements and a list to store duplicates
seen = set()
duplicates = []

# Iterate through the list
for item in str_list:
    if item in seen:
        duplicates.append(item)
    else:
        seen.add(item)

# Print the duplicates
print("Duplicate elements:", duplicates)
