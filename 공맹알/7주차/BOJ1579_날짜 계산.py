
e, s, m = map(int,input().split())

x = 1

while not (e == x % 15 and s == x %28 and m == x % 19):
    x+=1

print(x)

