def primary(n): 
    # 에라 어쩌고 체에 거르기
    arr = [1 for k in range(n+1)]

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            j = 2

        while i * j <= n:
            arr[i * j] = 0
            j += 1

    return arr

t = int(input())
nums = [int(input()) for _ in range(t)]
max_num = max(nums)
primarys = primary(max_num) 

for j in nums:
    result = 0

    for i in range(2, j // 2 + 1):
        if primarys[i] and primarys[j - i]:
            result += 1

    print(result)