n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr2 = sorted(arr,reverse=True)
for i in arr2:
    print(i,end=" ")