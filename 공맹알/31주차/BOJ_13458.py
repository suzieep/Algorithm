n = int(input());
arr = list(map(int, input().split()));
b, c = map(int, input().split());

ans = n; #총감독관 우선 세기

for a in arr:
    if a-b <= 0: #총감독관 1
        continue;
    else: #부감독관을 추가
        if a-b<=c:	#부감독관 1
            ans += 1;
        else:	#부감독관 1~
            mod = (a-b)%c;
            div = (a-b)//c;
            if mod == 0:
                ans += div;
            else:
                ans += div+1;

print(ans);