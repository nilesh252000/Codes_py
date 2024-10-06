#Within methods of same class
class Test:
    a=10
    def ram(self):
        print(self.a)
t1=Test()
t1.ram()

#Not accesable otside the class
'''class Test:
    __a=10
    def ram(self):
        pass
t1=Test()
t1.ram()
print(t1.__a)'''

# not acessiable Within methods of sub classes
class Test:
    __a=10
    def show(self):
         pass
class Test1(Test):
        def display(self):
            print(self.__a)
t=Test1()
t.display()
