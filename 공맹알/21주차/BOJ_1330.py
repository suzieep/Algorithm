a,b = map(int,input().split())
#각 경우에 따라 분기처리해주면 된다.
if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")