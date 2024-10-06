class Father:
    def __init__(self) -> None:
        print("cnstructor call")
class son(Father):
    def __init__(self) -> None:
        super().__init__()
        print("child class constructor")
t=son()
