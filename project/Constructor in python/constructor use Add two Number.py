class Add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.a+=self.b
    def display(self):
        print("Addition",self.a)
a=int(input("Enter the number"))
b=int(input("Enter the number"))
d1=Add(a,b)
d1.display()