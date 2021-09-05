#https://www.acmicpc.net/problem/5622

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
sec = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            sec += dial.index(i)+3 #다이얼 인덱스에 3 더해줘서 계산
print(sec)
