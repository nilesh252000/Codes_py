class Student:
    def ram(self,roll,name):
        self.roll=roll
        self.name=name
        print("Class Object Access Instance Variable",self.roll,self.name)
d1=Student()
d1.ram(1,'raju')
