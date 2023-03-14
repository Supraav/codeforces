n,t=input().split()
n=int(n)
t=int(t)
s=input().upper()
b=list(s)

# print(len(new_s))
# print(new_s)

while(t>0):
    i=0
    while i<len(b)-1:  
        if b[i]=='B' and b[i+1]=='G':            
            b[i],b[i+1]=b[i+1],b[i]      
            i+=1  
        i+=1
    t=t-1
final=''.join(b)
print(final)



#BGGBG
#GBGGB
