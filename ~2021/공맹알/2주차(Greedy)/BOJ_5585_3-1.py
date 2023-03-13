pay = int(input())

left = 1000-pay
money = [500,100,50,10,5,1]
cnt=0
for i in money:
    while left >= i:
        left -= i
        cnt+=1
        
print(cnt)
