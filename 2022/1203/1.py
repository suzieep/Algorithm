# from itertools
# def get_walk_min(diff_walk,m):
#     m_arr=[0]*100
#     for diff,walk in list(reversed(sorted(diff_walk))):
#         print(diff,walk)
        

def solution(infos, m):
    car_sum = 0 
    bike_sum = 0
    bike_walk_sum = 0
    public_sum = 0
    public_walk_sum = 0
    walk_sum = 0
    public_diff_walk = []
    bike_diff_walk = []

    for i in range(len(infos)):
        car_time,bike_time,public_time,walk_time = infos[i]
        car_sum += car_time
        bike_sum += bike_time
        if public_time>-1:
            public_sum += public_time
        else:
            public_sum += walk_time
            public_walk_sum += walk_time
        walk_sum += walk_time

        if public_time>walk_time and walk_time<(m-public_walk_sum):
            public_diff_walk.append((public_time-walk_time,walk_time))
        if bike_time>walk_time and walk_time<m:
            bike_diff_walk.append((bike_time-walk_time,walk_time))

    print(public_diff_walk,bike_diff_walk)        

    bike_sum = min(get_walk_min(bike_diff_walk,m),bike_sum)
    public_sum = min(get_walk_min(public_diff_walk,m-public_walk_sum),public_sum)


    answer = min(car_sum,bike_sum,public_sum,walk_sum)
    return answer
solution([[20, 40, -1, 60], [50, 20, 40, 30], [10, 30, 10, 20], [40, 10, 30, 50]], 60)
solution([[100, 80, 10, 20], [100, 60, -1, 40]], 30)


def dfs(board,edge,num,d,reach):
    is_visited = [False]*(len(board)+1)
    for i in range(1,len(board)+1):
        if board[edge][i]>0 and board[edge][i]<=d and not is_visited[i]:
            print(board)
            reach[i]=num
            dfs(board,i,num,d-board[edge][i],reach)
    return reach

def solution(n, edges, users, d, limit):
    board =[[0]*(n+1) for _ in range(n+1)]
    answer = 0

    for p1,p2,x in edges:
        board[p1][p2]=x
        board[p2][p1]=x

    reachs =[]

    for i in range(len(users)):
        if users[i]>0:
            dfs(board,i,users[i],d,[])    
    print(reach)


    return answer

    from itertools import combinations
INF =1e9

def get_walk_min(diff_walk,m):
    diff = 0
    m_arr=[0]*100
    combi=[i for i in diff_walk]
    for i in range(2,len(diff_walk)+1):
        # tmp = tuple(combinations(diff_walk,i))
        # print(tmp)
        for j in combinations(diff_walk,i):
            tmp_diff=0
            tmp_walk=0
            for k in j:
                tmp_diff+=k[0]
                tmp_walk+=k[1]
            if tmp_walk<=m:
                combi.append((tmp_diff,tmp_walk))
    if len(combi)>0:
        diff = max(combi)[0]
    return diff
        

def solution(infos, m):
    car_sum = 0 
    bike_sum = 0
    bike_walk_sum = 0
    public_sum = 0
    public_walk_sum = 0
    walk_sum = 0
    public_diff_walk = []
    bike_diff_walk = []

    for i in range(len(infos)):
        car_time,bike_time,public_time,walk_time = infos[i]
        car_sum += car_time
        bike_sum += bike_time
        if public_time>-1:
            public_sum += public_time
        else:
            if walk_time >(m-public_walk_sum):
                public_sum = INF
            else:
                public_sum += walk_time
                public_walk_sum += walk_time
        walk_sum += walk_time
        if walk_sum>m:
            walk_sum = INF

        if public_time>walk_time and walk_time<(m-public_walk_sum):
            public_diff_walk.append((public_time-walk_time,walk_time))
        if bike_time>walk_time and walk_time<m:
            bike_diff_walk.append((bike_time-walk_time,walk_time))


    bike_sum = bike_sum-get_walk_min(bike_diff_walk,m)
    public_sum = public_sum-get_walk_min(public_diff_walk,m-public_walk_sum)

    print(car_sum,bike_sum,public_sum,walk_sum)        

    answer = min(car_sum,bike_sum,public_sum,walk_sum)
    return answer