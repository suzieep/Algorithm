#40분
#floyd-warshall 
def floyd(graph,n):
    for i in range(1,n+1):
        graph[i][i]=0
        for j in range(1,n+1):
            for k in range(1,n+1):
                if not j==i or not k==i:
                    tmp = min(graph[j][k],graph[j][i]+graph[i][k])
                    graph[k][j]=tmp
                    graph[j][k]=tmp
    return graph

INF = int(1e9)
def solution(n, s, a, b, fares):
    answer = INF
    fares_arr = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for fare in fares:
        fares_arr[fare[0]][fare[1]]=fare[2]
        fares_arr[fare[1]][fare[0]]=fare[2]
    
    fares_arr=floyd(fares_arr,n)
    for i in range(1,n+1):
        answer=min(answer,fares_arr[s][i]+fares_arr[i][a]+fares_arr[i][b])
    
    return answer