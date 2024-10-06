#Within methods of same class
class Test:
    _a=10
    def ram(self):
        print(self._a)
t1=Test()
t1.ram()

#Within methods of outside class class
class Test:
    _a=10
    def ram(self):
        pass
t1=Test()
t1.ram()
print(t1._a)

#Within methods of sub classes
class Test:
    _a=10
    def show(self):
         pass
class Test1(Test):
        def display(self):
            print(self._a)
t=Test1()
t.display()

