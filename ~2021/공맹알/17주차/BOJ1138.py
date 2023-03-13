n = int(input())
arr = list(map(int,input().split()))
print(arr)
ans=[]

for i in range(n):
    ans.insert(arr[n-1-i],n-i)

#n-1-i로 해당 위치에 n-i를 넣어서 줄을 세워준다

print(*ans)
# *사용해서 배열에서 내용만 보이게 프린트 할 수 있다.