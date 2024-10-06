class Add:
    def __init__(self,a,b) -> None:
       self.a=a
       self.b=b
       def rdd(self):
           return self.a+self.b
           
a=int(input("Enter the number"))
b=int(input("Enter the number"))
D=Add(a,b)
sum=D.rdd()
print(sum)
