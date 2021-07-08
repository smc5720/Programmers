import itertools

def solution(numbers):
    comb = list(itertools.combinations(numbers, 2))
    tmp = set()

    for a, b in comb:
        tmp.add(a + b)
    
    answer = list(tmp)
    answer.sort()

    return answer