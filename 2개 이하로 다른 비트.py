# x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수를 반환한다.
def func(x):
    tmp = bin(x)
    # 편의를 위해 맨 앞에 0을 붙여준다.
    tmp = "0" + tmp[2:]
    # x가 짝수라면
    if x % 2 == 0:
        # 맨 끝은 항상 0일테니, 1을 더해준다.
        return x + 1
    # x가 홀수라면
    else:
        # 뒤에서부터 가장 먼저 나오는 0을 1로 바꿔주고
        # 그 뒤의 자리수를 0으로 바꿔준다.
        for i in range(len(tmp) - 1, -1, -1):
            if tmp[i] == "0":
                tmp = "0b" + tmp[:i] + "10" + tmp[i + 2:]
                return int(tmp, 2)


def solution(numbers):
    answer = []
    
    for i in numbers:
        answer.append(func(i))

    return answer
