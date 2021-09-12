def solution(dirs):
    answer = 0
    Y, X = 0, 1
    dir_dict = { 'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1] }
    # 시작은 가운데에서 한다.
    pos_y, pos_x = 5, 5
    visited = set()

    def visitable(y, x):
        return 0 <= y < 11 and 0 <= x < 11

    for i in dirs:
        dy = pos_y + dir_dict[i][Y]
        dx = pos_x + dir_dict[i][X]

        if not visitable(dy, dx):
            continue

        tmp1 = str(pos_y) + ", " + str(pos_x)
        tmp2 = str(dy) + ", " + str(dx)

        if (tmp1 + " " + tmp2) not in visited:
            visited.add(tmp1 + " " + tmp2)
            visited.add(tmp2 + " " + tmp1)
            answer += 1

        pos_y, pos_x = dy, dx

    return answer