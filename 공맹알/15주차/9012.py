count = int(input())
for i in range(count):
    content = input()
    list_a = list(content)
    sum = 0
    
    # 왼쪽일때는 sum을 더하고 오른쪽일땐 sum을 빼서 sum이 0이면 yes를 출력
    for i in list_a:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
        