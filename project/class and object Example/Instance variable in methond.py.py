class Demo:
    def dis(self):
        self.p="10"
        print("value is ",self.p)
d1=Demo()
d1.dis()
Demo.dis(d1)
