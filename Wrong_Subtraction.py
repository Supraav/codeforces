n,k=map(int,input().split())
a=k
while(a!=0):
    if(n%10==0):
        n=n//10
    else:
        n=n-1
    a-=1    

print (abs(n))

