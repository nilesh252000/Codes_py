'''class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        class Emp(Person):
            def __init__(self, name, age, eno, esal):
#Constructor Override
                super().__init__(name, age)
                self.eno=eno
                self.esal=esal
                def display(self):
                    print('Employee Name:', self.name)
                    print('Employee Age:', self.age)
                    print('Employee Number:', self.eno)
                    print('Employee Salary:', self.esal)
                    e1=Emp('Surabhi', 18, 1002,26000)
                    e1.display()
                    e2=Emp('Ranjith',20,1001,36000)
                    e2.display()'''


class Father:
    def __init__(self) -> None:
        self.money=100
        print("Father class constructor")
    def show(self):
        print("Father class Instance methond")
class Son(Father):
    def __init__(self) -> None:
        super().__init__()
        print("Son class constructor")
    def disp(self):
        print("Son class instance methond")
s=Son()