# 문제 : t로 도착한 시간을 받고, r로 우선순위를 받아서 우선순위와 시간을 고려하여 입장 순서를 출력한다.

def solution(t, r):
    answer = []
    arr=[]
    temp=[]

    for i in range(len(t)):
        arr.append([i,t[i],r[i]])
    time=0
    cnt=0
    print(arr)  

    while cnt != len(arr):
        for i in arr:
            if -1<i[1]<=time:
                # 현재 시간에 대해서 누적되는 사람을 temp에 저장
                temp.append(i)
        

        if temp:
            #temp에 남은 사람이 있을 경우 temp에서 우선순위가 가장 높은 사람을 입장시킨다.
            cnt+=1
            temp.sort(key = lambda x : int(x[2]))
            answer.append(temp[0][0])
            arr[temp[0][0]]=[-1,-1,-1]
            # -1을 넣어서 리셋 시킹
            temp=[]
        time+=1
        
    print(answer)
    
        
    return answer
solution([7,6,8,1],[0,1,2,3])