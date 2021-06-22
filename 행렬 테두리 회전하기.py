import copy


def print_board(board):
    print("-- print board --")
    for i in board:
        print(i)


def solution(rows, columns, queries):
    # rows * columns 크기의 행렬을 만든다.
    board = [[(r * columns) + c + 1 for c in range(columns)] for r in range(rows)]
    answer = []
    # 회전하려는 테두리의 상, 하, 좌, 우를 저장한다.
    for UP, LEFT, DOWN, RIGHT in queries:
        tmp = 10000
        UP, LEFT, DOWN, RIGHT = UP - 1, LEFT - 1, DOWN - 1, RIGHT - 1
        tmp_board = [[0 for _ in range(columns)] for _ in range(rows)]
        for y in range(0, rows):
            for x in range(0, columns):
                if y == UP:
                    if LEFT < x <= RIGHT:
                        tmp_board[y][x] = board[y][x - 1]
                        tmp = min(tmp_board[y][x], tmp)
                        continue
                if x == LEFT:
                    if UP <= y < DOWN:
                        tmp_board[y][x] = board[y + 1][x]
                        tmp = min(tmp_board[y][x], tmp)
                        continue
                if x == RIGHT:
                    if UP < y <= DOWN:
                        tmp_board[y][x] = board[y - 1][x]
                        tmp = min(tmp_board[y][x], tmp)
                        continue
                if y == DOWN:
                    if LEFT <= x < RIGHT:
                        tmp_board[y][x] = board[y][x + 1]
                        tmp = min(tmp_board[y][x], tmp)
                        continue
                tmp_board[y][x] = board[y][x]
        board = copy.deepcopy(tmp_board)
        answer.append(tmp)
    
    return answer