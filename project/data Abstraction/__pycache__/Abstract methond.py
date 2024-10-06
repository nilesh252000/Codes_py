from abc import ABC,abstractmethod
#Abstract class
class First(ABC):
    self.a=21
    self.b=33
    self.c=self.a+self.b
    @abstractmethod
    def show(self):
          pass
class Second(First):
        def show(self):
             print("Addition",self.c)
d=Second()
d.show()
d.show()