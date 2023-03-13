a,b,v=map(int,input().split())
t = (v-b)/(a-b) #시간초과 방지
print(int(t) if t == int(t) else int(t)+1) #나머지 있으면 하루 추가
