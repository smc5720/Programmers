from collections import deque

# 거리두기 여부를 True와 False로 나타낸다.
def check(place, y, x):
    queue = deque()
    queue.append([y, x])
    table = [[-1 for _ in range(5)] for c in range(5)]
    table[y][x] = 0

    x_dir = [0, 0, -1, 1]
    y_dir = [-1, 1, 0, 0]

    def visitable(y, x):
        return 0 <= y < 5 and 0 <= x < 5 and table[y][x] == -1 and place[y][x] != "X"

    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            dx = nx + x_dir[i]
            dy = ny + y_dir[i]
            if visitable(dy, dx):
                if place[dy][dx] == "P":
                    return False
                table[dy][dx] = table[ny][nx] + 1
                if table[dy][dx] < 2:
                    queue.append([dy, dx])
    return True


def solution(places):
    answer = []

    def func(place):
        for y in range(5):
            for x in range(5):
                # 현 위치에 응시자가 존재한다면
                if place[y][x] == "P":
                    # 거리두기 상태를 확인한다.
                    if not check(place, y, x):
                        # 거리두기 상태가 올바르지 않다면
                        answer.append(0)
                        return
        answer.append(1)
        return
    
    for i in places:
        func(i)

    return answer