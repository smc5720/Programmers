import itertools
from collections import defaultdict

def solution(orders, course):
    answer = []

    for i in course:
        comb_dict = defaultdict(int)
        for j in orders:
            if len(j) < i:
                continue
            # 손님의 주문내역을 알파벳 순으로 정렬한다.
            j = list(j)
            j.sort()
            j = "".join(j)
            # combination 라이브러리를 사용하여 단품 메뉴 조합을 생성한다.
            tmp = itertools.combinations(j, i)
            # 단품 메뉴 조합 별로 주문된 횟수를 저장한다.
            for k in tmp:
                s = "".join(k)
                comb_dict[s] += 1
        # 요구한 개수들로 이루어진 조합이 존재하지 않는 경우도 있다.
        # 예를 들어, 모든 손님들이 3개로 이루어진 조합을 주문했다면 4개 이상으로 이루어진 조합은 존재할 수 없다.
        if len(comb_dict) == 0:
            continue
        # 가장 많은 주문 횟수를 변수에 저장하고, 변수와 같은 value를 가진 key 값을 추가한다. 
        max_val = max(comb_dict.values())
        if max_val < 2:
            continue
        for key, val in comb_dict.items():
            if val == max_val:
                answer.append(key)
    answer.sort()
    return answer