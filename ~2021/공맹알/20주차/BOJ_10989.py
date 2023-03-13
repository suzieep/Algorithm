# 가용 메모리가 적은 문제라 sys를 import하고, 배열을 먼저 선언해서 정렬을 arr에 직접 해줬다.
# 심지어 pypy3으로 하면 메모리 초과 나와서 python3으로 계산해줬다..

import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] >= 1:
        for j in range(arr[i]):
            print(i)

