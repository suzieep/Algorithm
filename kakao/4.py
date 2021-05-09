import heapq

def Dijkstra(graph,n,start,heap,dp):
    dp[start] = 0 
    heapq.heappush(heap,(0, start)) 
    while heap: 
        wei, now = heapq.heappop(heap) 
        if dp[now] < wei: 
            continue 
        for w, next_node in graph[now]: 
            next_wei = w + wei 
            if next_wei < dp[next_node]: 
                dp[next_node] = next_wei 
                heapq.heappush(heap,(next_wei,next_node))


def solution(n, start, end, roads, traps):
    heap = []
    dp = [1000]*(n+1)
    answer = 0
    graph = [[] for _ in range(n + 1)]

    for i in roads:
        graph[i[0]].append((i[2],i[1]))

    Dijkstra(graph,n,start,heap,dp)


    return answer

solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3])