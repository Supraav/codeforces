a=input()
up_count=0
low_count=0
for x in a:
    if x.isupper():
        up_count+=1
    
    if x.islower():
        low_count+=1

# print(up_count,low_count)


if(up_count>low_count):
    a=a.upper()
else:
    a=a.lower()

print(a)




