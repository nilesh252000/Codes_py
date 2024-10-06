#Within methods of same class.
class Test:
    a=10
    def ram(self):
        print(self.a)
t1=Test()
t1.ram()

##Within methods of outside class

class Test:
    a=10
    def ram(self):
        print(self.a)
t1=Test()
t1.ram()
print(t1.a)

#Within methods of sub classes.
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

class Test:
    a=10
    def show(self):
         pass
class Test1(Test):
        def display(self):
            print(self.a)
t=Test1()
t.display()
