def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i]|arr2[i])[2:].rjust(n,"0").translate(str.maketrans('10', '# ')))
    return answer

    