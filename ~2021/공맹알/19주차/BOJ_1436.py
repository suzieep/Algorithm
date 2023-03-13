n = int(input())
cnt = 0
i = 665
while cnt < n:
    #str로 바꿔서 666이 있는 지 검사하고 brute force로 돌려준다
    i_s=str(i)
    if "666" in i_s:
        cnt+=1
        result=i_s
    i+=1
print(result)