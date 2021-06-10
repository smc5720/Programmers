def rotate_key(arr):
    return list(zip(*arr[::-1]))

# 현재 보드의 상태를 출력한다.
def show_board(board):
    print("-- show_board --")
    for i in range(len(board)):
        print(board[i])
    print("-- finish --")

# 키를 사용한다.
def attach_key(key, board, y, x, M):
    for i in range(M):
        for j in range(M):
            board[y + i][x + j] += key[i][j]

# 키를 뺀다.
def detach_key(key, board, y, x, M):
    for i in range(M):
        for j in range(M):
            board[y + i][x + j] -= key[i][j]

# 현재 lock이 풀렸는지 확인한다.
def check_board(M, N, board):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True
    M = len(key)
    N = len(lock)

    # 맵의 크기를 (키의 크기 * 2 + lock의 크기)로 설정했다.
    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]

    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    for k in range(4):
        key = rotate_key(key)
        for y in range(M + N):
            for x in range(M + N):
                attach_key(key, board, y, x, M)
                if check_board(M, N, board):
                    return True
                detach_key(key, board, y, x, M)
    
    return False