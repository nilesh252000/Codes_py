##Acessing elements list for loop use without  index
num_list = [21, 13, 17, 39, 17, 51]

for i in num_list:
    print(i)

##Acessing elements list for loop use index
    '''num_list = [21, 13, 17, 39, 17, 51]
    r=len(num_list)
    for i in range(r):
        print(i,num_list[i])'''
    
    my_list = [1, 2, 3, 4, 5]
number_to_find = 3

for item in my_list:
    if item == number_to_find:
        print("Found it!")
        break
else:
    print("Not found")
