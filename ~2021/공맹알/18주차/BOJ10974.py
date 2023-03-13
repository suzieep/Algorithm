import itertools
n = int(input())
arr=[]

for i in range(n): 
    arr.append(i+1) 
    per = itertools.permutations(arr, n) 
for i in per: 
    print(*i)

# permutations 써야하는 건 기억 났는 데 쓰는 법 기억 안나서 찾아서 풀었다.