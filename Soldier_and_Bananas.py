s=input()
a=s.split()
k=int(a[0])
n=int(a[1])
w=int(a[2])

val=int((k*(w*(w+1)/2))-n)
if val<0:
    print(0)
else:
    print(val)
