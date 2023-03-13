x = list(str(input()))

# 30 = 2*3*5 이므로 0이 필수로 있어야 첫째 자리에 0을 넣을 수 있음
# 그리고 0을 포함한 3자리가 3의 배수여야 한다.
# 2,3 자리에 3의 배수가 되는 가장 큰 수가 되어야 한다. 3의 배수인 2자리 수 중 가장 큰 수 부터 돌려서 있는 지 확인하기.

num = 3
arr =[]
while num!=99:
    arr.append(list(str(num)))
    num = num+3
result=[]

if '0' not in x:

    for i in arr:
        #얕은 복사를 위해 
        new = x[:]
        new.remove('0')
        if len(i)>1 and i[0] in new and i[1] in new:
            new.remove(i[0])
            new.remove(i[1])
            new.sort(reverse=True)
            st = new+i
            st.append('0')
            st=''.join(st)
            result.append(st)
        elif len(i)==1 and i[0] in new:
            new.remove(i[0])
            new.sort(reverse=True)
            st = new+i
            st.append('0')
            st=''.join(st)
            result.append(st)

if not result:
    print(-1)
else:
    result.sort(reverse=True)
    print(result[0])



