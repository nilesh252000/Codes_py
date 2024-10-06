class mobile:
    def __init__(self):
        self.model='realme'
    def show_model(self):
        print(self.model)
realme=mobile()
redmi=mobile()
greek=mobile()
print(realme.model)
print(redmi.model)
print(greek.model)
print()

redmi.model='readme4'
print(realme.model)
print(redmi.model)
print(greek.model)
print()
