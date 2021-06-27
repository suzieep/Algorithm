
name = list(input())
name_set = sorted(set(name))
cnt = [0]*len(name_set)

odd = 0
#홀수 갯수 세서 홀수 1개 혹은 0개일 때만 펠어쩌구 만들 수 있음

for i in range(len(name_set)):
    cnt[i]=name.count(name_set[i])

#갯수를 name_set이랑 같은 인덱스에다 세어줌
for i in cnt:
    if i%2!=0:
        odd += 1
        mid = cnt.index(i)

print(cnt,odd)

if odd>1:
    print("I'm Sorry Hansoo")
elif odd==1:
    # 틀리고 찾은 반례 : aaaaabbbb 이면 답이 ababababa가 되어야 하는데 가운데에 박아버림
    center=name_set[mid]*cnt[mid]
    del name_set[mid]
    result=sorted(list(name_set))
    print(''.join(result),end='')
    print(center,end='')
    print(''.join(sorted(result,reverse=True)))

else:
    result=sorted(list(name_set))
    print(''.join(result),end='')
    print(''.join(sorted(result,reverse=True)))


