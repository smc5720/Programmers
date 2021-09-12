def print_board(board):
    print("-- print board --")
    for i in board:
        print(i)

# 윗 행을 왼쪽에서 오른쪽으로 회전시키는 함수이다.
def rotate_right(board, UP, LEFT, DOWN, RIGHT, min_val):
    tmp = board[UP][RIGHT]
    min_val = min(min_val, tmp)
    for x in range(RIGHT, LEFT, -1):
        board[UP][x] = board[UP][x - 1]
        min_val = min(min_val, board[UP][x])
    return tmp, min_val

# 오른쪽 열을 위에서 아래로 회전시키는 함수이다.
def rotate_down(board, UP, LEFT, DOWN, RIGHT, num, min_val):
    tmp = board[DOWN][RIGHT]
    min_val = min(min_val, tmp)    
    for y in range(DOWN, UP, -1):
        board[y][RIGHT] = board[y - 1][RIGHT]
        min_val = min(min_val, board[y][RIGHT])
    # 중복된 값을 올바른 값으로 바꿔준다.
    board[UP + 1][RIGHT] = num
    return tmp, min_val

# 아랫 행을 오른쪽에서 왼쪽으로 회전시키는 함수이다.
def rotate_left(board, UP, LEFT, DOWN, RIGHT, num, min_val):
    tmp = board[DOWN][LEFT]
    min_val = min(min_val, tmp)
    for x in range(LEFT, RIGHT):
        board[DOWN][x] = board[DOWN][x + 1]
        min_val = min(min_val, board[DOWN][x])
    # 중복된 값을 올바른 값으로 바꿔준다.
    board[DOWN][RIGHT - 1] = num
    return tmp, min_val

# 왼쪽 열을 아래서 위로 회전시키는 함수이다.
def rotate_up(board, UP, LEFT, DOWN, RIGHT, num, min_val):
    for y in range(UP, DOWN):
        board[y][LEFT] = board[y + 1][LEFT]
        min_val = min(min_val, board[y][LEFT])
    # 중복된 값을 올바른 값으로 바꿔준다.
    board[DOWN - 1][LEFT] = num
    return min_val


def solution(rows, columns, queries):
    # rows * columns 크기의 행렬을 만든다.
    board = [[(r * columns) + c + 1 for c in range(columns)] for r in range(rows)]
    answer = []
    # 회전하려는 테두리의 상, 하, 좌, 우를 저장한다.
    for UP, LEFT, DOWN, RIGHT in queries:
        min_val = 10000
        UP, LEFT, DOWN, RIGHT = UP - 1, LEFT - 1, DOWN - 1, RIGHT - 1
        # 값을 잃는 문제가 발생하기 때문에 값을 저장해줘야 한다.
        tmp, min_val = rotate_right(board, UP, LEFT, DOWN, RIGHT, min_val)
        tmp, min_val = rotate_down(board, UP, LEFT, DOWN, RIGHT, tmp, min_val)
        tmp, min_val = rotate_left(board, UP, LEFT, DOWN, RIGHT, tmp, min_val)
        min_val = rotate_up(board, UP, LEFT, DOWN, RIGHT, tmp, min_val)
        answer.append(min_val)
    
    return answer