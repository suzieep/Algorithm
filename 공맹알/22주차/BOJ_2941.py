dic =["c=","c-","dz=","d-","lj","nj","s=","z="]
cnt = 0
x = str(input())

for i in dic:
    while i in x:
        # 다 replace 하면 cnt 하기 까다로워서 replace("찾을값", "바꿀값", [바꿀횟수]) 바꿀 횟수를 1번으로 지정해줌
        x=x.replace(i,' ',1)
        cnt +=  1
#원래 떨어져 있었다가 다른 문자가 빠지면서 지워져서 붙어서 인식되는 경우 제거 하기 위해 띄어쓰기 넣어줬다가 마지막에 세기 전에 빼줌
x = x.replace(' ','')
cnt += len(x)

print(cnt)

