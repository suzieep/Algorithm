n, m = map(int, input().split())

mins = []
for i in range(n):
    arr = list(map(int, input().split()))
    mins.append(min(arr))

print(max(mins))