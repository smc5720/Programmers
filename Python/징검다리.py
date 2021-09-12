def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()

    def func(gap):
        prev = 0
        cnt = 0
        for i in range(0, len(rocks)):
            if rocks[i] - prev < gap:
                cnt += 1
            else:
                prev = rocks[i]
        return cnt
    
    left = 0
    right = 1000000000

    while left <= right:
        mid = (left + right) // 2
        if func(mid) > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer