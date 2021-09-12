def check(k, stones, friend):
    # 출발지점: -1(0, 1, 2) / 도착지점: len(stones)(-3, -2, -1)
    index = -1
    # 디딤돌의 최대 간격을 의미한다.
    gap = 0
    for i in range(len(stones)):
        # friend는 mid 값, 징검다리를 건너고자 하는 총 인원을 나타낸다.
        if stones[i] >= friend:
            gap = max(gap, i - index)
            index = i
    # 디딤돌의 최대 간격이 k보다 클 경우 전원이 통과할 수 없다.
    gap = max(gap, len(stones) - index)
    if gap > k:
        return False
    return True


def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000

    # 이분탐색을 활용하여 문제를 해결한다.
    while left <= right:
        mid = (left + right) // 2
        if check(k, stones, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer