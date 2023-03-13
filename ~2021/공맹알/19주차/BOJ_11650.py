n= int(input())
arr=[]
for i in range(n) :
    x,y=map(int,input().split())
    arr.append((x,y))

#key 람다함수 사용해서 tuple 앞부터 정렬하도록 설정
arr.sort(key=lambda x : (x[0], x[1]))

for i in range(n):
    print(*arr[i])