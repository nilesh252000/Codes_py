a=int(input("Enter the number"))
count=0
i=1
while(i<=a):
    if(a%i==0):
        count+=1
    i+=1
if(count==2):
    print("number is prime")
else:
    print("number is not prime")
