class Demo:
   def method1(self):
     a=100 #Local Variable of method1
     print(a)
     def method2(self):
       b=200 #Local Variable of method2
       print(b)
       print(a) #'a' is local variable of method1()
d=Demo()
d.method1()
d.method2()