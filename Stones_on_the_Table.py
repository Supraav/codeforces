a=int(input())
count=0
stones=input()
# for i in range(a):
#     stones.append(input())

# stones=''.join(stones)
# print(stones)

for x in range(a-1):
    if stones[x]==stones[x+1]:
        count+=1

print(count)


