# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque 

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if not city in cache:
            answer+=5
        else:
            answer+=1
        cache.append(city)
        if len(cache)>cacheSize:
            cache.popleft()
    return answer

