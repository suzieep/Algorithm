n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split()))
left= 0
right = max(arr)
x = 0
while(left <= right):
    total = 0
    mid = (left + right)//2
    
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        x = mid 

print(x)