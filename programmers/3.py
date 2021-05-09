def solution(maps, p, r):
    answer=0
    ans=[0]*((len(maps))**2)

    dyx =[[0,1],[0,-1],[1,0],[-1,0]]
    half_yx=[[0,0],[1,0],[0,1],[1,1]]
    full_yx=[]
    for k in range(len(maps)-2):
        for i in range(len(dyx)):
            dy=half_yx[i][0]+dyx[i][0]
            dx=half_yx[i][1]+dyx[i][1]

            full_yx.append(half_yx[i])
            half_yx.append((dy,dx))

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

    for y in range(len(maps)):
        for x in range(len(maps[0])):

            for i in half_yx:
                ny= y + i[0]
                nx= x + i[1]
                if -1<ny<len(maps) and -1<nx<len(maps) and maps[ny][nx]<=(p/2):
                    ans[y*(len(maps))+x]+=1

            for i in full_yx:
                ny= y + i[0]
                nx= x + i[1]
                if -1<ny<len(maps) and -1<nx<len(maps) and maps[ny][nx]<=p:
                    ans[y*(len(maps))+x]+=1

    answer = max(ans)
    print(answer)
    return answer
solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]],19,6)