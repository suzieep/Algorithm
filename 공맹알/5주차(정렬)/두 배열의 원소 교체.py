n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sort_a = sorted(a)
sort_b = sorted(b,reverse=True)

for i in range(k):
    if sort_a[i]>sort_b[i]:
        break
    sort_a[i],sort_b[i]  = sort_b[i],sort_a[i]
    
sum=0
for i in range(n):
    sum+=sort_a[i]

print(sum)