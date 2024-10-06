for n in range(1,1001):
    sum=0
    temp=n
    while(temp>0):
        rem=temp%10
        sum+=(rem*rem*rem)
        temp//=10
    if(sum==n):
        print(n)
    n+=1
