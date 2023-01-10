from heapq import heappush
from itertools import combinations

def solution(cost, x):
    result = 0
    case = []
    costs = []
    cost_dic ={}
    
    for i in range(len(cost)):
        if cost[i]<=x:
            heappush(costs,(2**i,cost[i]))
        
    # print(costs)
    sum_combi=[]
    for i in range(len(costs)-1):
        combi= list(combinations(costs,i+2))
        # print(combi)
        for j in range(len(combi)):
            tmp_list=list(combi[j])
            tmp_cost = sum(com[1] for com in tmp_list)
            if tmp_cost <=x:
                tmp_count = sum(com[0] for com in tmp_list)
                sum_combi.append(tmp_count)
    if len(sum_combi)==0:
        if len(costs)==0:
            return 0
        return max(costs)[0]%(10**9+7)
    return max(sum_combi)%(10**9+7)