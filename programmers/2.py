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
                temp.append(i)

        if temp:
            cnt+=1
            temp.sort(key = lambda x : int(x[2]))
            answer.append(temp[0][0])
            arr[temp[0][0]]=[-1,-1,-1]
            temp=[]
        time+=1
        
    print(answer)
        
    return answer
solution([7,6,8,1],[0,1,2,3])