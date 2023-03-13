a,b,c,x,y = map(int,input().split())

if a + b < 2 * c: # 반반이 더 비싸면 그냥 각각 사기
    print(a * x + b * y)
else: #반반이 더 싸면 1) 갯수의 최솟값에 곱하고, 남은 갯수에 대해 계산
    print(2 * c * min(x, y) + min(a, 2 * c) * max(0, x - y) + min(b, 2 * c) * max(0, y - x))
