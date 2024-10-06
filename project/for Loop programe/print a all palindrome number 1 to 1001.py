for i in range(1,100):
    sum=0
    temp=i
    while(temp>0):
        rem=temp%10
        sum=(sum*10)+rem
        temp//=10
    if(sum==i):
        print(i)