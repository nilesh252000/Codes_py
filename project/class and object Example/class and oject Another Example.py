class Add:
    def Add1(self,a):
        self.a+=a
        return self.a
D=Add()
a=int(input("Enter the number"))
c=D.Add1(a)
print(c)