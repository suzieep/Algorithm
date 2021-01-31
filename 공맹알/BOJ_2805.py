n,m = map(int, input().split())
trees = list(map(int, input().split()))

left = 1
right = max(trees)

while left <= right:
    mid = (left+right) // 2
    sum = 0 
    for i in trees:
        if i >= mid:
            sum += i - mid
    if sum >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)