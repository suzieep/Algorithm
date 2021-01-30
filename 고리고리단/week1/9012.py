count = int(input())
for i in range(count):
    content = input()
    list_a = list(content)
    sum = 0
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
        