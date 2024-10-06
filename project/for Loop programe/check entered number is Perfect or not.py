a=int(input("Enter the numbe"))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum+=i
if(a==sum):
    print("number is perfect")
else:
    print("number is not perfect")