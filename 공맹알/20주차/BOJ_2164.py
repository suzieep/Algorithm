n = int(input())
arr = []
for i in range(1,n+1):
    arr.append(i)
    
# 처음꺼 지우고 다음꺼 temp에 저장하고 append
while len(arr)>1:
    del arr[0]
    temp = arr[0]
    del arr[0]
    arr.append(temp)

print(arr[0])