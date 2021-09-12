from collections import deque

# 현재 위치가 이동할 수 있는 곳인지 확인한다.
def is_visitable(N, Y, X, board):
    return 0 <= X < N and 0 <= Y < N and board[Y][X] == 0


def solution(board):
    answer = []
    N = len(board)
    # 새로 알게된 BFS 코딩 방식이다.
    Y, X, DIR, SUM = 0, 1, 2, 3
    LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
    # 반복문에서 쉽게 사용하기 위해 아래 배열을 만든다.
    course = [(0, -1, LEFT), (0, 1, RIGHT), (-1, 0, UP), (1, 0, DOWN)]
    # (Y, X) 위치의 최소값을 딕셔너리 형태로 저장한다.
    field = {(0, 0): 0}
    queue = deque()

    if board[0][1] == 0:
        field[(0, 1)] = 100
        queue.append([0, 1, RIGHT, 100])
    if board[1][0] == 0:
        field[(1, 0)] = 100
        queue.append([1, 0, DOWN, 100])

    while queue:
        tmp = queue.popleft()
        # 현재 값이 도착 위치라면 현재까지의 최소값을 저장한다.
        if tmp[Y] == N - 1 and tmp[X] == N - 1:
            answer.append(tmp[SUM])

        for dy, dx, d in course:
            # 현 위치로의 마지막 이동 방향과 이동하려는 방향이 같다면 100을 더해준다. 
            if tmp[DIR] == d:
                next_p = [tmp[Y] + dy, tmp[X] + dx, d, tmp[SUM] + 100]
            else:
                # 현 위치로의 마지막 이동 방향과 이동하려는 방향이 다르다면 600을 더해준다.
                next_p = [tmp[Y] + dy, tmp[X] + dx, d, tmp[SUM] + 600]
            # 튜플 형태, 딕셔너리의 key로 쉽게 활용하기 위해 만들어 놓는다.
            check = (next_p[Y], next_p[X])

            if is_visitable(N, next_p[Y], next_p[X], board):
                # 현재까지 이동경로의 최소값이 원래 저장된 최소값보다 크다면 더 이동할 의미가 없다.
                if check in field and field[check] < next_p[SUM]:
                    continue
                queue.append(next_p)
                field[check] = next_p[SUM]

    return min(answer)