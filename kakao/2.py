# 문제 : P는 앉기, 0는 빈자리, X는 가림막일 때, 가림막 없이 맨하튼 거리가 2 이하인 사람이 있을 경우 거리두기를 지키지 않은 상황이다.
# 주어지는 여러개의 2차원 배열에서 각각 거리두기가 지켜졌는지 아닌지에 따라 1,0으로 출력한다.
def solution(places):
    answer = [1,1,1,1,1]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    # 상하좌우를 저장해주고

    place =[]
    
    for n in places:
        for m in n:
            place.append(list(m))
        # 우선 여러개의 2차원 배열이 places에 합쳐져 있기 때문에 place로 나누어 준다
        
        for y in range(len(place)):
            for x in range(len(place[0])):
                #place를 0,0부터 끝까지 도는데, P인 곳을 찾는다.
                if place[y][x]=='P':
                    for i in range(len(dx)):
                        #P가 있는 곳에서 상하좌우의 정보를 저장하고
                        ny = y + dy[i]
                        nx = x + dx[i]
                        #P의 상하좌우에 P가 있으면 거리두기가 지켜지지 않았기 때문에 0 저장
                        if 5>ny>-1 and 5>nx>-1 and place[ny][nx]=='P':
                            answer[places.index(n)]=0
                        #P의 상하좌우에 0가 있으면 0의 상하좌우에 P가 저장되어있으면 0을 저장한다
                        if 5>ny>-1 and 5>nx>-1 and place[ny][nx]=='0':
                            for j in range(len(dx)):
                                ty = ny + dy[j]
                                tx = nx + dx[j]
                                # 단 원래 P가있었던 위치는 제외한다.
                                if 5>ty>-1 and 5>tx>-1 and ty!=y and tx!=x and place[ty][tx]=='P':
                                    answer[places.index(n)]=0
                            
        place=[]
    print(answer)
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])