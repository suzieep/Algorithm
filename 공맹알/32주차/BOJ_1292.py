arr = []
for i in range(1, 46): #46번을 반복하면 1000보다 작은 가장 큰 수
    arr += [i] * i
    
A, B = map(int, input().split())
print(sum(arr[A-1:B])) #a부터 b까지 모두 더해주자