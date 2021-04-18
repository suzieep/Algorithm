a=1
b=1
c=1

while(a+b+c!=0):
    a,b,c = map(int, input().split())
    if(a+b+c==0):
        break
    if(a**2+b**2==c**2):
        print("right")
    else:
        print("wrong")
