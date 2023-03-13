#https://www.acmicpc.net/problem/10039

a = [0]*5
 
for i in range(5):
    a[i] = int(input())
    
    if a[i] < 40:
        a[i] = 40
        
avg  = sum(a)/5    #평균 연산   
print(int(avg))
 
 
 
