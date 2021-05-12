def solution(n, times):
    answer = 0

    def func(time):
        cnt = 0
        for i in times:
            cnt += time // i
        return cnt

    left_point = 1
    right_point = 1000000000000000000

    while left_point <= right_point:
        mid = (left_point + right_point) // 2
        if func(mid) >= n:
            answer = mid
            right_point = mid - 1
        else:
            left_point = mid + 1

    return answer