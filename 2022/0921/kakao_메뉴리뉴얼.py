#백만년의 시간..
from itertools import combinations
from itertools import chain

def solution(orders, course):
    answer = []
    menu_cnt =[0]*26
    menu=''
    for i in orders:
        for j in i:
            menu_cnt[ord(j)-65]+=1
    for i in range(len(menu_cnt)):
        if menu_cnt[i]>0:
            menu+=chr(i+65)
            
    combi_result=[[] for _ in range(course[-1]+1)]
    combi_total=[]
    dic ={}
    for i in course:
        combi_result[i]=list(combinations(''.join(sorted(menu)),i))
    combi_total = list(chain(*combi_result))
    
    maxs = [0]*(course[-1]+1)
    
    for i in combi_total:
        tmp=''.join(i)
        dic[tmp]=0
        for j in orders:
            if set(tmp) < set(j):
                print(tmp,j)
                dic[tmp]=dic[tmp]+1
    print(dic)
    for key,value in dic.items():
        maxs[len(key)]=max(maxs[len(key)],value)
    print(maxs)
    for i in course:
        if maxs[i]>0 :
            for key,value in dic.items():
                if value==maxs[i] and i==len(key):
                    answer.append(key)
    print(answer)
    return answer