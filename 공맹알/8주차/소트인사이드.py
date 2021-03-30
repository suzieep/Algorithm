n = int(input())
arr = list(map(int,str(n)))
arr.sort(reverse=True)
for x in arr:
    print(x,end="")