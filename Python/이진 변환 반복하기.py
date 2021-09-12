def solution(s):
    # 이진 변환의 횟수를 의미한다.
    cnt = 0
    # 변환 과정에서 제거된 모든 0의 개수를 의미한다.
    zero_cnt = 0

    while s != "1":
        cnt += 1
        # 문자열의 모든 0을 제거한다.
        tmp = 0
        for i in s:
            if i == "0":
                tmp += 1
        zero_cnt += tmp

        # 문자열의 길이를 c라고 한다.
        c = len(s) - tmp

        # C를 2진법으로 표현한다.
        s = bin(c)
        s = s[2:]
    
    answer = [cnt, zero_cnt]

    return answer