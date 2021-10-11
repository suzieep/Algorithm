n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() # 정렬
print(arr[k - 1]) # k번째 수 출력