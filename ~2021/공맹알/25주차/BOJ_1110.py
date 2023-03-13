x = list(input())

cnt=0

def func(left,right): #왼쪽 수 오른쪽 수로 나눠서 func에 재귀
    global cnt 
    cnt+=1
    l=right

    r=(left+right)%10

    if l ==int(x[0]) and r==int(x[1]):
        print(cnt)
        return 0;
    func(l,r) # 다시 재귀
    
    
    
if len(x)<2:
    x=[0,x[0]] # 1의 자리 숫자일 때 앞에 0 넣어주기

func(int(x[0]),int(x[1])) # int 로 바꿔주기

