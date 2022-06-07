n=int(input())
a=[]
b=[]
for i in range(n):
    val1,val2=list(map(int,input().split()))
    a.append(val1)
    b.append(val2)
# print(a,b)


first=0
max=0
for j in range(n):
    first=first-a[j]+b[j]
    if first>max:
        max=first
print(max)

    