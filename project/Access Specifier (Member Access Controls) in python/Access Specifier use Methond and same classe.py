class Add:
    a=10
    _b=10
    __c=10
    def Add1(self):
        self.d=self.a+self._b+self.__c
        print("Addtion is",self.d)
s=Add()
s.Add1()
print(s.a)
print(s._b)
print(s.__c)

