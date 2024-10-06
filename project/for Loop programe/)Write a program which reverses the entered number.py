num=int(input("Enter the number"))
reverse=0
for i in range(0,len(str(num))):
    lastdigit=num%10
    reverse=(reverse*10)+lastdigit
    num=num//10
print("reverse number",reverse)