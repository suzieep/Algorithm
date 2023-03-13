def binary_search(array,left,right,target):
    while left<=right:
        mid = (left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        elif array[mid]>target:
            right=mid-1
    return None

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    x = binary_search(arr1,0,n-1,i)
    if x != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')