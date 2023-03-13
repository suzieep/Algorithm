
n = int(input())
arr = list(map(int,input().split()))
y=0
m=0
for i in arr:
    #각각 30,60으로 나누어떨어지는 값에 1을 더해서 금액을 곱해주면 된다.
    y += ((i // 30) + 1) * 10
    m += ((i // 60) + 1) * 15

if y<m:
    print("Y",y)
elif y>m:
    print("M",m)

else:
    print("Y","M",y)
