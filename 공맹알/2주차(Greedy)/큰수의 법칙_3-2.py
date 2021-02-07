n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
res=0
arr.sort(reverse = True)

while m!=0:
    res+=arr[0]*k
    m-=k
    res+=arr[1]
    m-=1

print(res)