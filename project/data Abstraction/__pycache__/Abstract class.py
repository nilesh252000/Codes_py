from abc import ABC,abstractmethod
#Abstract class
class First(ABC):
    @abstractmethod
    def show(self):
        pass
class Second(First):
        def show(self):
            self.a=21
            self.b=33
            self.c=self.a+self.b
            print("Addition",self.c)
d=Second()
d.show()