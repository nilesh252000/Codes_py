class A:
    a=10
    b=10
class B(A):
    def sum1(self):
        self.a+=self.b
        print(self.a)
class C(A):
    def sum2(self):
        self.a-=self.b
        print(self.a)
t=B()
t1=C()
t.sum1()
t1.sum2()

