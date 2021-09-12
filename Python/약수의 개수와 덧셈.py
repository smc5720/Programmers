import math


def solution(left, right):
    answer = 0

    min_val = int(math.sqrt(left))
    max_val = int(math.sqrt(right))

    for i in range(left, right + 1):
        answer += i
    
    for i in range(min_val, max_val + 1):
        if i ** 2 >= left:
            answer -= 2 * (i ** 2)

    return answer