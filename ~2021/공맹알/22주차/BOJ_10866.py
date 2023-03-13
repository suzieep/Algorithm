result =[]
deque=[]

def push_front(x):
    deque.insert(0,x)

def push_back(x):
    deque.append(x)

def pop_front():
    if deque:
        result.append(deque[0])
        del deque[0]
    else:
        result.append(-1)

def pop_back():
    if deque:
        result.append(deque.pop(-1))
    else:
        result.append(-1)

def size():
    result.append(len(deque))

def empty():
    if deque:
        result.append(0)
    else:
        result.append(1)

def front():
    if deque:
        result.append(deque[0])
    else:
        result.append(-1)

def back():
    if deque:
        result.append(deque[-1])
    else:
        result.append(-1)

n = int(input())
for i in range(n):
    
    arr = list(map(str,input().split()))
    #param 들어올 때랑 아닐 때 len으로 판단해서 함수 호출해주기
    if len(arr)>1:
        #string으로 함수 호출하는 법 arr[0]부분이 string 함수 이름 arr[1]이 param
        locals()[arr[0]](arr[1])
    else:
        locals()[arr[0]]()


print(*result,sep='\n')
