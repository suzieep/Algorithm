temp = 0
_range = int(input())
cnt = _range

for i in range(1,_range+1):
    in_list = str(i)
    for j in range(len(in_list)-1):
        now = int(in_list[j+1])-int(in_list[j])
        if j != 0:
            if temp!=now:
                cnt -= 1
        temp = now

print(cnt)