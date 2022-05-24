

for i in range(0,5):
    arr = [int(x) for x in input().split()]
    
    for j in range(0,len(arr)):
        if arr[j] == 1:
            print(abs(2 - i) + abs(2 - j))
            exit
