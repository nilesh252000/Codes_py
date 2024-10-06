class Test:
    def display(self):
        print("ram")
    def display(self,a):
        print(self.a)
    def display(self,firstName='',LastName=""):
        print(firstName,LastName)
r=Test()
r.display()
r.display(10)
r.display("Nilesh","raju")

'''class Test:
    def display(self,a,b):
        self.a=a
        self.b=b
        self.a+=self.b
        print(self.a)
    def display(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.c=self.a+self.b+self.c
        print(self.c)
        
r=Test()
r.display(10,20)
r.display(10,20,30)'''

'''class Test:
    def show(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
        print(self.c)
    def Add(self,a):
        self.a=a
        print(self.a)

T=Test()
T.Add(10,20)
T.Add(10),'''
