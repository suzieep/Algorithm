arr = list(input())
left=0
right=0
for i in range(len(arr)//2): #길이의 절반을 나눔
    left += int(arr[i])#좌측 
    right += int(arr[len(arr)-1-i])#우측 각각 더해줌
if left==right:
    print("LUCKY")#일치하면
else :
    print("READY")

