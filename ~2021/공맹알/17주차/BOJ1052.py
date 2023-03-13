N, K = map(int, input().split())

ans = 0
# 결국 이진수랑 같은 개념이므로 bin 함수를 사용해서 구해줄 수 있다.

while bin(N).count('1') > K:
    a = 2 ** (bin(N)[::-1].index('1'))
    ans += a
    N += a
print(ans)