import math


def trans_10_to_3(n):
    tmp = ""
    s = int(math.log(n, 3))

    for i in range(s, -1, -1):
        a = 3 ** i
        r = n // a
        tmp += str(r)
        n -= a * r

    return tmp


def trans_3_to_10(s):
    tmp = 0
    for i in range(len(s) - 1, -1, -1):
        tmp += int(s[i]) * (3 ** i)

    return tmp


def solution(n):
    answer = trans_3_to_10(trans_10_to_3(n))
    return answer