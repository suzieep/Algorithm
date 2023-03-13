n = input()
arr = [0]*9 # 갯수 세어줄 자리 만들어주기
for i in n:
    i = int(i)
    if i == 9:
        i = 6
    arr[i] += 1
arr[6] = (arr[6]+1)//2 # 홀수일 때
print(max(arr)) # 가장 큰 값