a,b,c = map(int,input().split())
#sep으로 각각 줄에 프린트
print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n')
