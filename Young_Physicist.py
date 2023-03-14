n=int(input())
x=0
y=0
z=0
for i in range(n):
   
    n1,n2,n3=map(int,input().split())
    x+=n1
    y+=n2
    z+=n3

if(x==0) and (y==0) and (z==0):
    print("YES")
else:
    print("NO")