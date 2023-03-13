n ,k = map(int,input().split())
arr =list(map(int,input().split()))

tmp=0
for i in arr:
    if i%2==0:
        tmp+=i//2 #멀티탭이 짝수면 절반만큼 꼽을 수 있고
    else:
        tmp+=i//2+1 #멀티탭이 홀수면 절반+1만큼 꼽을 수 있는 걸 모두 더해준다

if tmp>=n:
    print("YES")
else:
    print("NO")