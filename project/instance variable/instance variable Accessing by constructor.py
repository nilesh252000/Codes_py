class MyClass:
    def __init__(self, a):
        # Accessing instance variable 'a' and assigning a value
        self.a = a

    def show(self):
        # Accessing instance variable 'a' within a method
        print("Value of 'a':", self.a)


# Creating an object of the class and passing a value to the constructor
obj = MyClass(10)

# Calling the 'show()' method to display the value of 'a'
obj.show()  # Output will be: Value of 'a': 10
