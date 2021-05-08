def solution(places):
    answer = []
    visited = [[False] * 5 for _ in range(5)]

    def init_visited():
        for y in range(0, 5):
            for x in range(0, 5):
                visited[y][x] = False

    def bfs(n, y, x, places):
        q = []
        x_dir = [0, 0, -1, 1]
        y_dir = [-1, 1, 0, 0]

        for i in range(0, 4):
            y_pos = y + y_dir[i]
            x_pos = x + x_dir[i]
            if y_pos < 0 or x_pos < 0 or y_pos >= 5 or x_pos >= 5:
                continue
            if visited[y_pos][x_pos] == False:
                visited[y_pos][x_pos] = True
                if places[n][y_pos][x_pos] != "X":
                    q.append([y_pos, x_pos])

        q2 = []
        while q:
            top = q.pop(0)
            if places[n][top[0]][top[1]] == "P":
                return 0
            elif places[n][top[0]][top[1]] == "O":
                for i in range(0, 4):
                    y_pos = top[0] + y_dir[i]
                    x_pos = top[1] + x_dir[i]
                    if y_pos < 0 or x_pos < 0 or y_pos >= 5 or x_pos >= 5:
                        continue
                    if visited[y_pos][x_pos] == False:
                        visited[y_pos][x_pos] = True
                        if places[n][y_pos][x_pos] != "X":
                            q2.append([y_pos, x_pos])
        
        while q2:
            top = q2.pop(0)
            if places[n][top[0]][top[1]] == "P":
                return 0
        return 1

    # n번 강의실
    for n in range(0, 5):
        state = True
        for y in range(0, 5):
            if state == False:
                break
            for x in range(0, 5):
                if places[n][y][x] == "P":
                    init_visited()
                    visited[y][x] = True
                    if bfs(n, y, x, places) == 0:
                        state = False
                        break
        if state:
            answer.append(1)
        else:
            answer.append(0)

    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])