class Add:
    def display(self,a,b):
        self.a+=self.b
        print("Addition two number",self.a)

d1=Add()
a=int(input("Enter the number"))
b=int(input("Enter the number"))
d1.display(a,b)