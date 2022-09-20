#lv2, 45m 75점
def solution(record):
    answer = []
    record_arr=[]
    uid = []
    name=[]
    for i in record:
        tmp=i.split()
        record_arr.append(tmp[:2])
        if len(tmp)==3:
            if tmp[1] in uid:
                name[uid.index(tmp[1])]=tmp[2]
            else:
                uid.append(tmp[1])
                name.append(tmp[2])
    for i in range(len(record_arr)):
        tmp_name=name[uid.index(record_arr[i][1])]
        if record_arr[i][0]=="Enter":
            answer.append(tmp_name+"님이 들어왔습니다.")
        elif record_arr[i][0]=="Leave":
            answer.append(tmp_name+"님이 나갔습니다.")
    return answer