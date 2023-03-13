arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(arr)):
    for j in range(i,0,-1):     # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break

print(arr)