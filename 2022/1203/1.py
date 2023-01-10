def get_walk_min(diff_walk,m):
    m_arr=[0]*100
    for diff,walk in list(reversed(sorted(diff_walk))):
        print(diff,walk)
        

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