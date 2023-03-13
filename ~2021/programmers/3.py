# 게임 프로그램을 만든다 n*n의 게임판에서 p(힘)와 r(반지름)을 주었을 때 그를 기준으로 마름모 선상에 있을 땐 p의 1/2의 크기로,
# 그 안의 경우 p의 크기로 에너지를 쓸 수 있고, 그 p이하의 에너지인 곳의 갯수를 센다. 어떤 위치를 중심으로 했을 때, 가징 많은 곳을 없앴을 때 그 값이 얼마인지 구하라
def solution(maps, p, r):
    answer=0
    ans=[0]*((len(maps))**2)

    dyx =[[0,1],[0,-1],[1,0],[-1,0]]
    #y,x를 기준으로 상하좌우 저장
    half_yx=[[0,0],[1,0],[0,1],[1,1]]
    #절반으로 힘을 받는 위치를 저장하고, 반지름을 한 칸 씩 늘릴 때마다 이 위치를 full_yx로 옮겨주어 확인하는 방식
    full_yx=[]
    for k in range(len(maps)-2):
        for i in range(len(dyx)):
            dy=half_yx[i][0]+dyx[i][0]
            dx=half_yx[i][1]+dyx[i][1]
            #좌표를 dx와 dy로 나타내어주고 half에 있는 것들을 full로 옮기고 half에는 현재 위치를 넣어준다.

            full_yx.append(half_yx[i])
            half_yx.append((dy,dx))

            #그냥 하나씩 넣어주기 위한 코드
            new_list = []
            for v in full_yx:
                if v not in new_list:
                    new_list.append(v)
            full_yx=new_list

            new_list = []
            for v in half_yx:
                if v not in new_list:
                    new_list.append(v)
            half_yx=new_list

# 맵을 한 칸씩 옆으로 돌아다닐 때를 for로
    for y in range(len(maps)):
        for x in range(len(maps[0])):

            #half자리를 다 훓어서 p/2보다 작은 곳을 확인해서 카운트를 세어주고
            for i in half_yx:
                ny= y + i[0]
                nx= x + i[1]
                if -1<ny<len(maps) and -1<nx<len(maps) and maps[ny][nx]<=(p/2):
                    ans[y*(len(maps))+x]+=1

            #full자리를 다 훓어서 p보다 작은 곳을 확인해서 카운트를 추가로 세어준다.
            for i in full_yx:
                ny= y + i[0]
                nx= x + i[1]
                if -1<ny<len(maps) and -1<nx<len(maps) and maps[ny][nx]<=p:
                    ans[y*(len(maps))+x]+=1

    #이때 리스트에서 맥스 출력
    answer = max(ans)
    print(answer)
    return answer
solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]],19,6)