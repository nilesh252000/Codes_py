a=int(input("Enter the number"))
for i in range(1,a):
    if(a%i==0):
        print("number is prime")
        break
    else:
        print("number is not prime")

a=int(input("Enter the number"))
sum=1
for i in range(1,a):
    if(a%i==0):
        sum+=1
if(sum==2):
    print("number is prime")
else:
    print("number is not prime")