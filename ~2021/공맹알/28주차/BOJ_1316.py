result = int(input())
for k in range(result):
    word = input()
    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]): #find함수를 이용해 단어를 찾아줌
            result -= 1
            break
print(result)