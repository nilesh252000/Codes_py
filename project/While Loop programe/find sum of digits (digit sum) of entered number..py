sum=0
a=int(input("Enter the number"))
i=0
while(a>0):
    r=a%10
    sum+=r
    a=a//10
print(sum)