
"""size = int(input("Enter the size of the square: "))
digit = input("Enter the digit to fill the square: ")
for i in range(size):
    for j in range(size):
        print(digit, end=' ')
    print()"""


# Number of rows
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()
