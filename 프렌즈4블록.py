from collections import deque

# 현재 좌표를 기준으로 4개 블록을 확인한다.
def check(y, x, board):
    x_dir = [0, 1, 1]
    y_dir = [1, 0, 1]
    
    for i in range(3):
        x_pos = x + x_dir[i]
        y_pos = y + y_dir[i]
        if x_pos >= len(board[0]) or y_pos >= len(board):
            return False
        if board[y][x] != board[y_pos][x_pos]:
            return False

    return True

# 사라진 블록들의 공백을 메꿔주는 함수이다.
def sort_board(board):
    for j in range(len(board[0])):
        for i in range(len(board) - 1, 0, -1):
            if board[i][j] == " ":
                idx = i - 1
                while idx >= 0 and board[idx][j] == " ":
                    idx -= 1
                if idx >= 0:
                    board[i][j] = board[idx][j]
                    board[idx][j] = " "


def solution(m, n, board):
    # 가로 길이: n
    # 세로 길이: m
    answer = 0
    state = True
    queue = deque()
    for i in range(m):
        board[i] = list(board[i])
    
    while state:
        state = False
        for i in range(m):
            for j in range(n):
                if board[i][j] != " " and check(i, j, board):
                    state = True
                    queue.append((i, j))
                    queue.append((i, j + 1))
                    queue.append((i + 1, j))
                    queue.append((i + 1, j + 1))
        # 사라질 블록들의 좌표를 queue에 담는다.
        while queue:
            y, x = queue.pop()
            if board[y][x] != " ":
                answer += 1
                board[y][x] = " "
                
        sort_board(board)
        
    return answer