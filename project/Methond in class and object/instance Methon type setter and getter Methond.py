class Student:
    def setName(self,name):
        self.name=name
    def GetName(self):
        return self.name
    def setMark(self,mark):
        self.mark=mark
    def Getmark(self):
        return mark
n=int(input("Enter the Number"))
for i in range(n):
    s=Student()
    name=str(input("Enter name"))
    s.setName(name)
    print("getStudentName",s.GetName())
    mark=int(input("Enter the Marks"))
    s.setMark(mark)
    print("GetMarks",s.Getmark())

