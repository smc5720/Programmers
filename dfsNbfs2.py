def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(n):
        for i in range(0, len(computers[n])):
            if visited[i] == False and computers[n][i] == 1:
                visited[i] = True
                dfs(i)

    for i in range(0, n):
        if visited[i] == False:
            visited[i] = True
            answer += 1 
            dfs(i)

    return answer