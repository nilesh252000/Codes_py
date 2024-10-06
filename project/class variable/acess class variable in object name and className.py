class MyClass:
    class_variable = "I am a class variable"

# Accessing class variable using class name
print(MyClass.class_variable)

# Creating an instance of the class
obj = MyClass()

# Accessing class variable using instance
print(obj.class_variable)
