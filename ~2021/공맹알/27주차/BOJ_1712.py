#https://www.acmicpc.net/problem/1712

a,b,c = map(int, input().split())

if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1)) # 연산 방식