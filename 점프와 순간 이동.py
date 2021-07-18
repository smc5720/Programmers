from collections import deque

def solution(n):
    ans = 0
    # n이 0이 될 때까지 반복한다.
    while n != 0:
        # n이 홀수라면
        if n % 2 == 1:
            # 1을 빼서 n을 짝수로 만든다.
            n -= 1
            # 건전지 사용량을 1 증가시킨다.
            ans += 1
        # n이 짝수라면
        else:
            # n을 2로 나눈다.
            n //= 2
    
    return ans