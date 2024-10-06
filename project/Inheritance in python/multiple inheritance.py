class Test:
    def disply(self):
        print("raju")
class Test1:
    def display1(self):
        print("ram")
class disply2(Test,Test1):
    pass

t=disply2()
t.disply()
t.display1()