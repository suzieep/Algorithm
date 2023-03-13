n, k = map(int, input().split()) 
q = [] 
result = [] 

for i in range(n): 
    q.append(i+1) 
    c = 0 
    
while len(q) >0:
    c = (c + (k-1)) % len(q)
    cc = q.pop(c) 
    result.append(str(cc))

print("<%s>" %(", ".join(result)))

