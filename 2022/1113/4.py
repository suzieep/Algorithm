from collections import defaultdict

def process():
    

def solution(jobs):
    answer = []
    t=1
    kind = jobs[0][2]
    importance_dic=defaultdict(int)
    jobs_by_kind =defaultdict(list)
    for i in range(len(jobs)):
        tmp_req,tmp_dur,tmp_kind,tmp_importance=jobs[i]
        if tmp_req<=t :
            importance_dic[tmp_kind]+=tmp_importance
            jobs_by_kind[tmp_kind].append(tmp_dur)
        print(i+1,jobs_by_kind,importance_dic)

        if i<len(jobs)-1 and t<jobs[i+1][0]:
            if not tmp_kind == kind:
                kind = max(sorted(importance_dic),key=importance_dic.get)
            importance_dic[kind]=0
            if len(answer)==0 or (len(answer)>0 and not answer[-1]== kind):
                answer.append(kind)
            t += sum(jobs_by_kind[kind])
            print(t)
            jobs_by_kind[kind]=[]
    return answer