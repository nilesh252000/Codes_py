class Add:
    def sum(self,a):
         self.a=a
         return self.a
D=Add()
a=int(input("Enter the number"))
r=D.sum(a)
print(r)