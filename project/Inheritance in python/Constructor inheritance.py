class Father:
    def __init__(self) -> None:
        self.a=100
    def disply(self):
        print("Instance methond")
class son(Father):
    def display1(self):
        print("sub instance methond")
t=son()
print(t.a)