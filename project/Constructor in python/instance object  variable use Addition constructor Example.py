class Add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.a+=self.b
    def display(self):
        print("Addition",self.a)
d1=Add(10,20)
d1.display()