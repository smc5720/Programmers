def solution(m, n, puddles):
    field = [[0] * (m + 1) for _ in range(n + 1)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for x, y in puddles:
        field[y][x] = 1
    
    dp[1][1] = 1
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if field[y - 1][x] == 0:
                dp[y][x] += dp[y - 1][x]
                dp[y][x] %= 1000000007
            if field[y][x - 1] == 0:
                dp[y][x] += dp[y][x - 1]
                dp[y][x] %= 1000000007
    
    return dp[n][m]