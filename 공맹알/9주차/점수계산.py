arr = []
for i in range (8):
    arr.append(int(input()))
arr.sort(reverse=True)

rank = []
for i in arr[:5]:
    rank.append(arr.index(i)+1)
rank.sort()

print(sum(arr[:5]))
print(*rank)