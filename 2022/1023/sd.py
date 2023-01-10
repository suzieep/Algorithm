
from collections import deque   

def bfs(cost,x,bought,count):
    queue = deque([x-1])     
    bought[x-1] = True       
    while queue:
        v = queue.popleft()     
        for i in range(v,-1,-1):   
            if not bought[i]:  
                queue.append(i) 
                bought[i]= True    
                
                
def dfs(cost,x,bought,count):
    for i in range(len(cost)-1,-1,-1):
        if cost[i]<=x and bought[i]==False:
            x -= cost[i]
            count += 2**i
            bought[i]=True
            count = dfs(cost,x,bought,count)
    return count            
        
    
def solution(cost, x):
    count = 0
    
    for i in range(len(cost),0,-1):
        bought = [False]*len(cost)
        tmp = dfs(cost,x,bought,0)
        count = max(count,tmp)
        tmp_2=bfs(cost,x,bought,count)
        count
    return count

    from collections import deque   

def bfs(cost,x,bought,count):
    queue = deque([x-1])     
    bought[x-1] = True       
    while queue:
        v = queue.popleft()     
        for i in range(v,-1,-1):   
            if cost[i]<x and not bought[i]:  
                queue.append(i) 
                count += 2**i
                bought[i]= True    
    
def solution(cost, x):
    count = 0
    
    for i in range(len(cost),0,-1):
        bought = [False]*len(cost)
        tmp = bfs(cost,x,bought,count)
        count = max(count,tmp)
    return count
    
    

