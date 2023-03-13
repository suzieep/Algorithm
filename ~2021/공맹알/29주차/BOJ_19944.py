n ,m = map(int,input().split())

if m==1 or m==2: #1학년이나 2학년
    print("NEWBIE!")
elif n>=m: # 뉴비가 아니면서 n보다 작은
    print("OLDBIE!")
else :
    print("TLE!")