#85점(시간초과)
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
            if set(tmp) <= set(j):
                dic[tmp]=dic[tmp]+1
    for key,value in dic.items():
        maxs[len(key)]=max(maxs[len(key)],value)
    for i in course:
        if maxs[i]>1 :
            for key,value in dic.items():
                if value==maxs[i] and i==len(key):
                    answer.append(key)
    return sorted(answer)