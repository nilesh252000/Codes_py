# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs to the dictionary
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'

print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}



# create dictionary in python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict)

#insert the elements in Dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict[67]="raju"
print(my_dict)

#another example to add element in dictionary in python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['name']="Nilesh"
print(my_dict)


#upadate the Dictionary in python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Before",my_dict)
x={'city':"pune"}
my_dict.update(x)
print("after",my_dict)

#delete the Dictionary Item in python
d={100:"durga",200:"ravi",300:"shiva"}
print("Before deletion")
print(d)

del d[100]
print("After the deletion")
print(d)
