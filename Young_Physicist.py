n=int(input())
count=0
for i in range(n):
    x=0
    y=0
    z=0
    x,y,z=([int(j) for j in input().split()])
    count=count+(x+y+z)
    
if count==0:
    print("YES")
else:
    print("NO")