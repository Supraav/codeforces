a= input().lower()
b=input().lower()

def prob():
    if(a<b):
        print("-1")
    elif(a>b):
        print("1")
    else:
        print("0")

if __name__=="__main__":
    prob()