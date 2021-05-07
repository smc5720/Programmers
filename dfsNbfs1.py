answer = 0

def solution(numbers, target):
    def dfs(idx, sum):
        if idx == len(numbers):
            if sum == target:
                global answer
                answer += 1
            return
        dfs(idx + 1, sum + numbers[idx])
        dfs(idx + 1, sum - numbers[idx])

    dfs(0, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))