class Add:
    def rdd(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
d=Add()
a=int(input("Enter the number"))
b=int(input("Enter the number"))
sum=d.rdd(a,b)
print(sum)
