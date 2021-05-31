from collections import deque
from collections import defaultdict
from itertools import product

# 이분탐색으로 n보다 큰 점수의 개수를 반환한다.
def find(arr, n):
    left = 0
    right = len(arr) - 1
    # 이 부분에서 시간을 많이 소요했다.
    # idx가 끝까지 초기화되지 않을 경우 어떤 값을 default로 사용할 건지 고민해볼 것
    idx = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= n:
           idx = mid
           right = mid - 1
        else:
            left = mid + 1
    return len(arr) - idx


def solution(info, query):
    answer = []
    q_dict = defaultdict(list)

    # 모든 경우의 수로 key를 만든다.
    # value로는 점수들의 배열을 만든다.
    for i in range(len(info)):
        info[i] = info[i].split()
        for j in range(len(info[i]) - 1):
            tmp = [info[i][j], "-"]
            info[i][j] = tmp[:]
        tmp = list(product(*info[i][:-1]))
        for j in tmp:
            # q_dict = {'javabackendjuniorpizza': [150], 'javabackendjunior-': [80, 150], 'javabackend-pizza': [150], ... }
            q_dict["".join(j)].append(int(info[i][-1]))
    
    for i in q_dict.keys():
        # 이분탐색을 위해 점수들의 배열을 정렬한다.
        q_dict[i].sort()
    
    for i in range(len(query)):
        tmp = query[i].split()
        query[i] = deque()
        for j in tmp:
            if j != "and":
                query[i].append(j)
        tmp = int(query[i][-1])
        query[i].pop()
        answer.append(find(q_dict["".join(query[i])], tmp))

    return answer