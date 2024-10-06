#Accessing the dictionary values
courses={1:'java',2:'python',3:'panda'}
print(courses[1])

# Access values from dictionary using get() method
print(courses.get('name'))


#use value  is Mutable in python
courses={1:'java',2:'python',3:'panda'}
courses[1]="raju"
print(courses)

#Allow only duplicatevalues, not keys

d={1:'A',2:'B',3:'C', 1:'A'}
d={1:'A',2:'B',3:'C', 4:'A'}
print(d)

#create an empty dictionary add an elements
d={}
d['a']="Apple"
d['b']="banana"
print(d)


