n=1
while(n<=100):
    sum=0
    i=1
    while(i<=n):
        if(n%i==0):
            sum+=1
        i+=1
    if(sum==2):
        print(n)
    n+=1