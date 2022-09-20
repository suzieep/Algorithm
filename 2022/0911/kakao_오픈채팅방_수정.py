#lv2, 50m
#시간초과로 Index 없애려고 딕셔너리 찾아서 수정
def solution(record):
    answer = []
    record_arr=[]
    user={}
    for i in record:
        tmp=i.split()
        record_arr.append(tmp[:2])
        if len(tmp)==3:
            if tmp[1] in user:
                user[tmp[1]]=tmp[2]
            else:
                user[tmp[1]]=tmp[2]
    for i in range(len(record_arr)):
        if record_arr[i][0]=="Enter":
            answer.append(user[record_arr[i][1]]+"님이 들어왔습니다.")
        elif record_arr[i][0]=="Leave":
            answer.append(user[record_arr[i][1]]+"님이 나갔습니다.")
    return answer