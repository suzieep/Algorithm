from collections import deque

def bfs(start,graph,qtype,a,b):
        q = deque()
        q.append(start)
        if qtype=='type_c':
            result_arr =[]
        while q:
            tmp = q.pop()
            if qtype=='type_c':
                qa = bfs(tmp,graph,"type_a",a,b)
                qb = bfs(tmp,graph,"type_b",a,b)
            for node in graph[tmp[0]]:
                if (qtype=='type_a' and node[0]==a)or(qtype=='type_b' and node[0]==b):
                    return node[1]+tmp[1]
                q.append((node[0],node[1]+tmp[1]))
            if qtype=='type_c':
                result_arr.append(tmp[1]+qa+qb)
        return min(result_arr)
    
def solution(n, s, a, b, fares):
    answer = 0
    fares_list = [[] for _ in range(n+1)]
    for fare in fares:
        fares_list[fare[0]].append([fare[1],fare[2]])
        fares_list[fare[1]].append([fare[0],fare[2]])
    cost = bfs([s,0],fares_list,"type_c",a,b)
    # print(cost)
    return answer