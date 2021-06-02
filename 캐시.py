from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    for i in cities:
        # 대소문자를 구분하지 않으므로 lower를 적용한다.
        i = i.lower()
        # cache hit
        if i in cache:
            del cache[cache.index(i)]
            cache.append(i)
            answer += 1
        # cache miss
        else:
            answer += 5
            cache.append(i)
            if len(cache) > cacheSize:
                cache.popleft()

    return answer