class Add:
    def __init__(self,a) -> None:
        self.a=a
    def display(self):
        return self.a

a=10
s=Add(a)
r=s.display()
print(r)