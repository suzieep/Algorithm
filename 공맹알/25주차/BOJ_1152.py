x = list(input())

if x[0]==' ':
    del x[0]
if len(x)>0 and x[-1]==' ': # 공백이 하나일 경우 len이 0이 되므로 처리를 해줘야함
    del x[-1]

print(x.count(' ')+1 if len(x)>0 else 0) #python 삼항연산자 사용 방법