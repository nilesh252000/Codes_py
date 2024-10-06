class A:
    a=10
class B(A):
    b=10
class c(B):
    def sum(self):
        self.a+=self.b
        print(self.a)
sum1=c()
sum1.sum()
