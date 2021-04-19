def solution(prices):
    answer = [-1] * len(prices)
    stack = []
    size = len(prices)

    for i in range(size):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = size - 1 - top

    return answer