
i=int(input("Enter the nuber"))
sum=0
orig=i
while(i>0):
    rem=i%10
    sum=sum+(rem*rem*rem)
    i=i//10
    
if(orig==sum):
    print("Number is Armstrong")
else:
    print("number is not Armstrong")