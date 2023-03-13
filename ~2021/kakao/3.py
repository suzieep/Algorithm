# 문제 : D 2는 선택을 밑으로 2칸, U 3은 선택을 위로 세칸, C는 현재 선택한 항을 삭제, Z는 마지막으로 삭제한 항을 복구한다.
# 이 때 주어진 문자열에 대해서 이를 수행하고 마지막에 순서대로 여전히 항이 존재하면 O, 삭제되었으면 X를 출력한다.


from collections import deque

def solution(n, k, cmd):
    answer=''
    ans=[]
    arr=[]
    now = k
    history=[]
    
    for i in range(n):
        arr.append(chr(65+i))
        
    q = deque(arr)
    
    for i in cmd:
        # 항의 첫글자에 D가 오면 밑으로 선택을, 항의 3번째 글자만큼 내려준다
        if i[0]=='D':
            now += int(i[2])
        # 항의 첫글자에 U가 오면 위로 선택을, 항의 3번째 글자만큼 내려준다
        if i[0]=='U':
            now -= int(i[2])
        # 이때 현재위치가 음수라면 한바퀴 돌려준다
        if now<0:
            now += len(q)
        #지울 때는 먼저 히스토리에 현재 항의위치와 정보를 저장하고 지워준다. 근데 만약 현재 위치가 넘어가면 위로 올려준다
        if i[0]=='C':
            history.append((now,q[now]))
            del q[now]
            if len(q)==now:
                now=0
        #히스토리에서 꺼내와서 큐에 다시 원래 자리에 넣어주고, 히스토리는 팝해준다.
        if i[0]=='Z':
            q.insert(history[-1][0],history[-1][1])
            history.pop()
            
    for i in arr:
        if i in q:
            ans.append('O')
        else:
            ans.append('X')

    answer=''.join(ans)
            
    return answer

solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])