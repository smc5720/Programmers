from collections import defaultdict
from collections import deque

def func(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    return a * b

# 후위표기법 계산
def calculate(s):
    s.reverse()
    stack = deque()
    while s:
        tmp = s.pop()
        if tmp != "+" and tmp != "-" and tmp != "*":
            stack.append(tmp)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(func(a, b, tmp))
    return abs(stack.pop())

def solution(expression):
    answer = 0
    op_dict = defaultdict(list)

    # 연산자의 우선순위가 작을수록 높다.
    op_dict["+"] = [1, 1, 2, 2, 3, 3]
    op_dict["-"] = [2, 3, 3, 1, 1, 2]
    op_dict["*"] = [3, 2, 1, 3, 2, 1]
    parse_ex = deque()

    # stack에 문자열을 파싱하는 과정
    tmp = ''
    for j in expression[:]:
        if j != "+" and j != "-" and j != "*":
            tmp += j
        else:
            parse_ex.append(int(tmp))
            parse_ex.append(j)
            tmp = ''
    parse_ex.append(int(tmp))
    
    # 중위 표기법을 후위 표기법으로 전환하는 과정
    for i in range(0, 6):
        tmp = deque()
        stack = deque()
        for j in parse_ex:
            if j != "+" and j != "-" and j != "*":
                tmp.append(j)
            else:
                if stack:
                    # 이 부분에서 가장 시간이 많이 걸렸다.
                    # 연산자가 들어오면 자기보다 우선순위가 높거나 같은 것들을 뺀다.
                    while stack and op_dict[stack[-1]][i] <= op_dict[j][i]:
                        tmp.append(stack.pop())
                    # 이후 자신을 스택에 담는다.
                    stack.append(j)
                # 피연산자가 들어오면 바로 담는다.
                else:
                    stack.append(j)
        while stack:
            tmp.append(stack.pop())
        answer = max(calculate(tmp), answer)

    return answer