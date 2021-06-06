import string
from collections import deque

# 알맞은 진법으로 변환하는 함수
def convert(num, base):
    tmp = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r] 
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    answer = ''
    num = 0
    s_size = 0
    arr = deque()
    # 전체 문자열의 크기가 (사람의 숫자 * 구할 숫자의 개수)까지만 있으면 된다.
    while s_size < t * m:
        tmp = convert(num, n)
        s_size += len(tmp)
        arr.append(tmp)
        num += 1
    idx = 1
    tmp = "".join(arr)
    # 알맞은 순서의 수를 저장한다.
    for i in tmp[:t * m]:
        if idx % m == p % m:
            answer += i
        idx += 1

    return answer