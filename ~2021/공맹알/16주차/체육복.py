def solution(n, lost, reserve):
    
    answer = 0
    answer = n - len(lost)
    
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            answer+=1
            
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
            
    return answer
