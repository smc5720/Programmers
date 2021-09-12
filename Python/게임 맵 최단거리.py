from collections import deque


def print_map(maps):
    print("--print map--")
    for i in maps:
        print(i)

# 해당 좌표가 방문할 수 있는 곳인지 확인한다.
def visitable(maps, y, x, r, c):
    return 0 <= x < c and 0 <= y < r and maps[y][x] == 1


def solution(maps):
    r = len(maps)
    c = len(maps[0])
    # 해당 위치까지의 최소 이동거리를 의미한다.
    table = [[-1 for _ in range(c)] for x in range(r)]
    # 출발점은 0, 0이다.
    start_y, start_x = 0, 0
    # 도착점은 4, 4이다.
    end_y, end_x = r - 1, c - 1
    
    table[start_y][start_x] = 1

    queue = deque()
    queue.append([start_y, start_x])

    x_dir = [-1, 1, 0, 0]
    y_dir = [0, 0, -1, 1]

    while queue:
        # 현재 좌표와 현 좌표까지의 최소 이동거리를 저장한다.
        now_y, now_x = queue.popleft()
        # 상하좌우로 방문한다.
        for i in range(4):
            dest_y = now_y + y_dir[i]
            dest_x = now_x + x_dir[i]
            if visitable(maps, dest_y, dest_x, r, c):
                if table[dest_y][dest_x] == -1:
                    table[dest_y][dest_x] = table[now_y][now_x] + 1
                    queue.append([dest_y, dest_x])

    return table[end_y][end_x]