from collections import deque

# 문자열 s가 올바른 괄호 문자열인지 확인한다.
def check(s):
    stack = deque()
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if i == "]" and stack[-1] == "[":
            stack.pop()
            continue
        if i == "}" and stack[-1] == "{":
            stack.pop()
            continue
        if i == ")" and stack[-1] == "(":
            stack.pop()
            continue
        stack.append(i)

    # stack에 값이 남아있으면 올바른 괄호 문자열이 아니다.
    if stack:
        return False
    return True


def solution(s):
    answer = 0
    
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        if check(tmp):
            answer += 1

    return answer