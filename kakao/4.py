import heapq

# 최단경로 찾기, 배열에 노드의 연결 방향 정보와 가중치가 나오고, 트랩을 가게되면 방향이 바뀐다. 최단거리를 구해라

# 경로찾기에 다익스트라가 제일 좋을 것 같아서 다익스트라 써줌
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

    #그래프에다가 노드와 방향정보를 넣어주고
    for i in roads:
        graph[i[0]].append((i[2],i[1]))
    
    #다익스트라 돌려줌
    answer = Dijkstra(graph,n,start,heap,dp)

    return answer

solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3])