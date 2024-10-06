sum=0
a=int(input("Enter the number"))
i=1
while(i<a):
    if(a%i==0):
        sum+=i
    i+=1
if(a==sum):
    print("number is perfect")
else:
    print("number is not perfect")
