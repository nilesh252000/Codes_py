class A:
    def Add(self,a,b):
        self.a=a
        self.b=b
        self.a+=self.b
class B(A):
    def Add2(self):
        print(self.a)
sum=B()
x=10
b=10
sum.Add(x,b)
sum.Add2()