arr = []
for _ in range(int(input())):
    word = input()
    if word not in arr:
        arr.append(word)
arr.sort() #사전순 정렬
arr.sort(key=lambda x : len(x)) #길이순 정렬
for word in arr:
    print(word)