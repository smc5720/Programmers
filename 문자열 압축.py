import math

def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        tmp = s
        sum_val = 0
        # 문자열을 ["aa", "aa", "bb", "cc"]의 형태로 저장한다.
        arr = []
        if len(s) % i != 0:
            max_idx = (len(s) // i) * i
            tmp = tmp[:max_idx]
            sum_val += len(s) - len(tmp)
        for j in range(0, len(tmp) // i):
            arr.append(s[j*i:j*i+i])
        # pop 연산 시간복잡도 향상을 위해 리스트를 거꾸로 뒤집는다.
        arr.reverse()
        cur = ""
        # 변수 cnt는 현재 문자열을 얼마나 압축시킬 수 있는지를 저장한다.
        cnt = 0
        # 현재 문자열과 arr의 -1번째 원소가 같다면 압축이 가능하다.
        # cur = "aa" | arr = ["cc", "bb", "aa"] | "2aa" + ["cc", "bb"]
        while arr:
            if cur == "":
                cur = arr.pop()
                cnt = 1
                continue
            if cur == arr[-1]:
                cnt += 1
                arr.pop()
            else:
                if cnt > 1:
                    sum_val += int(math.log10(cnt)) + 1
                sum_val += len(cur)
                cur = arr.pop()
                cnt = 1
        if cnt > 1:
            sum_val += int(math.log10(cnt)) + 1
        sum_val += len(cur)
        # 현재 문자열의 길이와 cnt를 이용해 줄어든 문자열의 길이를 계산한다.
        answer = min(answer, sum_val)
        # 최소 값을 갱신해준다.

    return answer