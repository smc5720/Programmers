from collections import deque


def get_new_pos(pos, board):
    direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    n_pos = []
    y1, x1 = pos[0]
    y2, x2 = pos[1]
    # 상하좌우로 이동한다.
    for dy, dx in direc:
        if [board[y1 + dy][x1 + dx], board[y2 + dy][x2 + dx]] == [0, 0]:
            n_pos.append({(y1 + dy, x1 + dx), (y2 + dy, x2 + dx)})
    # 가로에서 세로로 변경한다.
    if y1 == y2:
        for dy, dx in direc[2:]:
            if [board[y1 + dy][x1 + dx], board[y2 + dy][x2 + dx]] == [0, 0]:
                n_pos.append({(y1, x1), (y1 + dy, x1)})
                n_pos.append({(y2, x2), (y2 + dy, x2)})
    # 세로에서 가로로 변경한다.
    if x1 == x2:
        for dy, dx in direc[:2]:
            if [board[y1 + dy][x1 + dx], board[y2 + dy][x2 + dx]] == [0, 0]:
                n_pos.append({(y1, x1), (y1, x1 + dx)})
                n_pos.append({(y2, x2), (y2, x2 + dx)})
    return n_pos


def print_board(board):
    print("--print board--")
    for i in board:
        print(i)


def solution(board):
    answer = 0
    n = len(board)
    board = [[1] + b + [1] for b in board]
    board = [[1] * (n + 2)] + board + [[1] * (n + 2)]
    
    pos = {(1, 1), (1, 2)}
    queue = deque()
    visited = []

    queue.append([pos, 0])
    visited.append(pos)

    while queue:
        pos, dist = queue.popleft()
        dist += 1
        for n_pos in get_new_pos(list(pos), board):
            if (n, n) in n_pos:
                return dist
            if n_pos not in visited:
                visited.append(n_pos)
                queue.append([n_pos, dist])
    return -1