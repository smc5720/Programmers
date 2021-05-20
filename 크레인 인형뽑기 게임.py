def solution(board, moves):
    stack = []
    field = [[] for _ in range(len(board))]
    answer = 0

    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board)):
            if board[i][j] != 0:
                field[j].append(board[i][j])

    for i in moves:
        tmp = i - 1
        if field[tmp]:
            cur_block = field[tmp].pop()
            if stack and stack[-1] == cur_block:
                stack.pop()
                answer += 2
            else:
                stack.append(cur_block)

    return answer