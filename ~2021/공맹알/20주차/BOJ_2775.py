#배열을 선언해주고 아래층부터 인원수를 더해나가는 형식으로 풀 수 있다.

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    arr = [ i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1,n):
            arr[j] += arr[j-1]
    print(arr[-1])


