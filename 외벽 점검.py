from itertools import permutations
from collections import deque


def func(case, weak):
    min_val = len(case) + 1
    idx = len(weak) // 2
    for i in range(0, idx):
        # 출발지의 위치를 다르게 하면, 도착지도 달라져야 한다.
        tmp = deque(weak[i:i+idx])
        start = weak[i]
        min_val = min(min_val, cal(case, start, tmp))
    return min_val

# 반복문 관리를 쉽게 하기 위해 일부러 함수를 한번 더 나눴다.
def cal(case, start, tmp):
    cnt = 0
    for j in case:
        # 친구 한명 더 투입
        cnt += 1
        # 친구가 커버 가능한 지역을 queue에서 제거
        while start + j >= tmp[0]:
            tmp.popleft()
            # queue가 비었다면 취약 지점을 모두 확인한 것
            if not tmp:
                return cnt
        start = tmp[0]
    # 친구가 모두 투입되었는데도 취약 지점이 남아있다면 불가능한 방법이므로 무한대 반환
    return float("inf")


def solution(n, weak, dist):
    answer = len(dist) + 1
    # 친구가 배치될 수 있는 모든 경우의 수를 지정한다.
    all_cases = list(permutations(dist))
    # 시계 방향과 반시계 방향을 쉽게 고려하기 위해 배열의 크기를 2배로
    for i in weak[:]:
        # 4에서 출발해 반시계 방향으로 7만큼 돌면 9에 도착한다.
        # = 9에서 출발해 시계 방향으로 7만큼 돌면 4에 도착한다.
        # 외벽 길이가 12일 경우, 9에서 출발해 4에 도착한다는 것은, 9에서 7만큼 이동한 16이 4와 같다는 뜻이다.
        # 따라서 [1, 3, 4, 8, 9, 10]에 "각 원소 + 외벽 길이"를 붙여준다.
        #[1, 3, 4, 8, 9, 10, 12 + 1, 12 + 3, 12 + 4, 12 + 8, 12 + 9, 12 + 10]
        weak.append(i + n)
    
    for i in all_cases:
        answer = min(answer, func(i, weak))
    
    if answer == len(dist) + 1:
        return -1
    return answer