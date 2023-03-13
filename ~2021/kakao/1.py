# 문제 : 1zero3oneeight으로 입력되면 10308로 출력하기

def solution(s):
    answer = 0
    # 영어 이름 모두 저장해두기
    dic =['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    x = []
    temp=[]
    for i in s:
        #아래에서 저장한 temp가 존재할 때 만약 temp가 dic안에 있는 원소와 일치하면 dic의 인덱스를 답 배열에 넣는다
        if temp:
            for j in dic:
                if j == ''.join(temp):
                    x.append(str(dic.index(j)))
                    temp=[]

        # 문자열을 하나씩 차례로 읽어서 숫자인지 아닌지 확인해준다 숫자면 답배열에 넣고
        if i.isdigit():
            x.append(i)
        #숫자가 아니면 temp에 저장한다
        else:
            temp.append(i)
            print(temp)
    print(x)
    t = ''.join(x)
    print(t)

    return answer

solution('one4seveneight')