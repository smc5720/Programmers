from collections import defaultdict
from collections import deque
from itertools import combinations

# 리스트가 유일성을 만족하는가를 판단한다.
def func(s):
    r_dict = defaultdict(int)
    for i in range(len(s)):
        r_dict[s[i]] += 1
    for val in r_dict.values():
        if val > 1:
            return False
    return True

# True: a는 b의 부분집합이다.
# False: a는 b의 부분집합이 아니다.
def check(a, b):
    for i in a:
        if i not in b:
            return False
    return True


def solution(relation):
    answer = deque()
    tmp = [i for i in range(len(relation[0]))]

    # comb에는 가능한 조합이 저장된다.
    # comb = [(0), (1), (2), (3), (0, 1), (0, 2), ... , (0, 1, 2, 3)]
    comb = deque()
    for i in range(1, len(relation) + 1):
        for j in list(combinations(tmp, i)):
            comb.append(j)

    # pop의 속도를 높이기 위해 리스트를 뒤집는다.
    comb.reverse()
    tmp = deque()

    while comb:
        arr = deque()
        for i in range(len(relation)):
            st = ""
            for j in comb[-1]:
                st += relation[i][j]
            arr.append(st)
        # 최소성 만족 여부를 판별한다.
        # answer에 저장된 조합이 포함된 조합식은 최소성을 만족하지 않는다.
        if func(arr):
            state = True
            for i in answer:
                if check(i, comb[-1]):
                    state = False
                    break
            if state:
                # answer에는 유일성과 최소성을 모두 만족한 조합이 저장된다.
                answer.append(comb[-1])
        comb.pop()
        
    return len(answer)