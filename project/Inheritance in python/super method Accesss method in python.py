class Father:
    def show(self):
        print("Father class Instance methond")
class Son(Father):
        def show(self):
             super().show()
             print("Son class instance methond")
s=Son()
s.show()