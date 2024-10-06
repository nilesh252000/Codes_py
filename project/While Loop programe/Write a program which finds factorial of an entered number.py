a = int(input("Enter the number: "))
i = 1
f = 1  # Starting with 1 for multiplication

while i <= a:  # Loop should run while i is less than or equal to the number
    f *= i
    i += 1

print(f)
