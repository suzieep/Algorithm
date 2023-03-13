
#모르겠어서 블로그 보면서 따라함

arr=[]

while True:
    a = int(input())
    if(a == 0):
        break
    arr.append(a)

prime= [0]*1000001
check = [0]*1000001
cnt = 0

for i in range(2,1000001):
    if(check[i] == 0):
        cnt = cnt+1
        prime[cnt] = i
    for j in range(i*i,1000001,i):
        check[j]= 1

def check_prime(n): # 에라토스테네스의 체
    k=1
    while True:
        if(prime[k] ==0): #나타낼 수 없음
            print("Goldbach's conjecture is wrong.")
            break
        if(check[n-prime[k]]==0):
            print(n,'=',prime[k],'+',n-prime[k])
            break
        k=k+1

for i in range(0,len(arr)):
    check_prime(arr[i])