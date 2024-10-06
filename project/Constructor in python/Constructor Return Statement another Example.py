class Add:
    def __init__(self,a,b) -> None:
       self.a=a
       self.b=b
       self.a+=self.b
       return self.a    
a=int(input("Enter the number"))
b=int(input("Enter the number"))
D=Add(a,b)
