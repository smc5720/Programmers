# 일치하는 숫자의 개수를 넣으면 알맞은 등수를 반환한다.
def func(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    elif num <= 1:
        return 6


def solution(lottos, win_nums):
    answer = []
    zero_num = 0
    col_num = 0

    for i in lottos:
        if i == 0:
            zero_num += 1
        if i in win_nums:
            col_num += 1
    
    answer.append(func(col_num + zero_num))
    answer.append(func(col_num))

    return answer