arr = [0]*100

def fibonacci(x):
    if x==1 or x==2:
        return 1
    if arr[x]!=0:
        return arr[x]
    arr[x] =fibonacci(x-1) + fibonacci(x-2)
    return arr[x]

print(fibonacci(6))