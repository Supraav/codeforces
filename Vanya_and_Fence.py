n,h=input().split()
n=int(n)
h=int(h)
# print(n,h)
width=0
lst = [int(x) for x in input().split()]
for i in lst:
    if i<=h:
        width+=1
    else:
        width+=2

print(width)