num=int(input("Enter the number"))
c=num
reverse=0
for i in range(0,len(str(num))):
    lastdigit=num%10
    reverse=(reverse*10)+lastdigit
    num=num//10
if(c==reverse):
    print("number is palindrome")
else:
    print("Number is not paildrom")