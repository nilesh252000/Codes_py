class Test:
    def Add(self):
        self.a=10
        self.b=12
        self.a+=self.b
class Test1(Test):
    def Add(self):
        print(self.a)
        print("raju")
        
r=Test1()
r.Add()
