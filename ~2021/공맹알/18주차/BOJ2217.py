n = int(input())
arr=[]
res = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in range(n):
    res.append(arr[i]*(i+1))
    

print(max(res))

# 처음엔 min값에다가 n 곱하면 되겠지 싶어서 그렇게 계산했는데 로프 사용 안해도 된다는 말 보고 다시 풀어야했다.
# 최소값 하나씩 빼면서 res에 저장하고 그 중 최대하중을 뽑아내는 식으로 바꿔주었다.=> 시간초과..;
# min 사용량을 줄이기 위해 sort를 하고 결론을 내는 방식으로 바꿔줬다.