def binary_search(arr,left,right,target):

    if left > right:
        return None         # 엉키면 return None
    mid = (left+right)//2   # 정수형으로 다루기 위해서 //쓰는 거 잊지 않기!

    if target==arr[mid]:
        return mid
    elif arr[mid]<target:
        return binary_search(arr,mid+1,right,target)   # mid는 아니니까 그 뒤부터 해주기
    elif target<arr[mid]:
        return binary_search(arr,left,mid-1,target)    # mid는 아니니까 그 앞부터 해주기
    

n,t= map(int, input().split())
array = list(map(int, input().split()))
array.sort()
print(binary_search(array,0,len(array)-1,t)+1)  # 인덱스니까 +1 