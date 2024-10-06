class Add:
    def Add1(self):
        self.a=10
        self.b=20
        self.a+=self.b
    def display(self):
        print("Addition",self.a)
d1=Add()
d1.Add1()
d1.display()