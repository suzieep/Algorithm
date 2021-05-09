#문제 : 문자열을 맨아랫줄처럼 받고 code와 day가 일치하는 항의 Price를 시간순으로 출력한다.

def solution(code, day, data):
    answer = []
    arr = [[0 for k in range(3)] for k in range(len(data))]

    for i in data:
        idx = data.index(i)
        temp=[]
        t=0
        i+=' '
        for j in i:
            #숫자일 경우에는 temp에 한글자씩 넣어주고
            if j.isdigit():
                temp.append(j)
            #만약 띄어쓰기를 만나면 temp를 저장하고 비워주는 식으로 문자열을 배열에 넣어 정리해준다.
            if j==' ':
                arr[idx][t]=''.join(temp)
                temp=[]
                t+=1
    #받은 arr를 시간에 따라 정렬하고 코드와 데이가 맞는 경우를 return해준다
    arr.sort(key = lambda x : int(x[2]))
    for i in arr:
        if i[1]==code and i[2][0:8]==day:
            answer.append(i[0])
    print(answer)

    return answer

solution("012345","20190620",["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"])