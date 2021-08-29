while True:
        a = list(map(int, input().split()))
        max_num = max(a)
        if sum(a) == 0:
            # 다 0 나오면 끝내기
                break
        a.remove(max_num)
        if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
            #직각삼각형 공식 맞으면 right
                print('right')
        else:
                print('wrong')