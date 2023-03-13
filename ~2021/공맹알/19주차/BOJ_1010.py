
import math

case = int(input())
#조합 공식으로 팩토리얼을 사용해서 풀어준다.

for i in range(case):
    r,n =map(int,input().split())
    c = math.factorial(n-r)
    b = math.factorial(n)
    a = math.factorial(r)
    print(b//(a*c))