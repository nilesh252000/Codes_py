a=1
while(a<=100):
    sum=0
    temp=a
    while(temp>0):
        rem=temp%10
        sum=(sum*10)+rem
        temp//=10
    if(sum==a):
        print(a)
    a+=1
    