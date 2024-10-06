a=int(input("Enter the number"))
c=a
sum=0
while(a>0):
    rem=a%10
    sum=(sum*10)+rem
    a=a//10
if(c==sum):
    print("number is palindrome")
else:
    print("number is not palindrome")
