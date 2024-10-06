a=12
def fun1():
    print("global variable inside",a)
def fun2():
    print("global variable otside",a)
fun1()
fun2()