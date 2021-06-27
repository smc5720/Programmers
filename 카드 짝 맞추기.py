from collections import defaultdict
from collections import deque
from itertools import permutations

answer = float("inf")

def visitable(y, x):
    return 0 <= x < 4 and 0 <= y < 4

# 카드의 종류를 넣으면 해당 카드를 보드에서 제거한다.
def remove_card(board, card_pos, card_kind):
    for i in range(2):
        y, x = card_pos[card_kind][i]
        board[y][x] = 0


# 카드의 종류를 넣으면 해당 카드를 보드에서 복구한다.
def restore_card(board, card_pos, card_kind):
    for i in range(2):
        y, x = card_pos[card_kind][i]
        board[y][x] = card_kind


def ctrl_move(board, y, x, direc):
    left, right, up, down = 0, 1, 2, 3
    y_dir = [0, 0, -1, 1] 
    x_dir = [-1, 1, 0, 0]
    ny, nx = y, x
    while True:
        tmp_y = ny + y_dir[direc]
        tmp_x = nx + x_dir[direc]
        if not visitable(tmp_y, tmp_x):
            return ny, nx
        if board[tmp_y][tmp_x] != 0:
            return tmp_y, tmp_x
        ny, nx = tmp_y, tmp_x


def bfs(board, start_y, start_x, des_y, des_x):
    if [start_y, start_x] == [des_y, des_x]:
        return start_y, start_x, 1
    # table은 현재 위치부터 해당 좌표까지의 최소 이동 횟수를 저장한다.
    table = [[0 for _ in range(4)] for a in range(4)]
    visited = [[False for _ in range(4)] for a in range(4)]
    queue = deque()
    queue.append([start_y, start_x])
    visited[start_y][start_x] = True
    y_dir = [0, 0, -1, 1]
    x_dir = [-1, 1, 0, 0]

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            # 먼저 상하좌우로 움직이는 경우이다.
            now_y, now_x = y + y_dir[i], x + x_dir[i]
            # 방문 가능한 곳이라면
            if visitable(now_y, now_x) and not visited[now_y][now_x]:
                # 방문 여부를 True로 설정하고
                visited[now_y][now_x] = True
                # 이동 횟수를 저장한다.
                table[now_y][now_x] = table[y][x] + 1
                if [now_y, now_x] == [des_y, des_x]:
                    return now_y, now_x, table[now_y][now_x] + 1
                queue.append([now_y, now_x])

            # 이후에는 ctrl 이동을 고려한다.
            now_y, now_x = ctrl_move(board, y, x, i)
            # 방문 가능한 곳이라면
            if not visited[now_y][now_x]:
                # 방문 여부를 True로 설정하고
                visited[now_y][now_x] = True
                # 이동 횟수를 저장한다.
                table[now_y][now_x] = table[y][x] + 1
                if [now_y, now_x] == [des_y, des_x]:
                    return now_y, now_x, table[now_y][now_x] + 1
                queue.append([now_y, now_x])
    return start_y, start_x, float("inf")


# rmv_card_num: 없어진 카드 쌍의 수를 의미한다.
# ord_idx: 현재 사용할 orders idx를 의미한다.
def backtracking(board, card_pos, orders, start_y, start_x, rmv_card_num, ord_idx, count):
    global answer
    if rmv_card_num == len(card_pos.keys()):
        answer = min(answer, count)
        return
    # 현재 제거하려는 카드의 종류를 저장한다.
    card_kind = orders[ord_idx][rmv_card_num]

    card1_y, card1_x = card_pos[card_kind][0][0], card_pos[card_kind][0][1]
    card2_y, card2_x = card_pos[card_kind][1][0], card_pos[card_kind][1][1]

    # 한 쌍의 카드에서 첫번째 카드를 먼저 지우는 경우이다.
    ry1, rx1, cnt1 = bfs(board, start_y, start_x, card1_y, card1_x)
    ry2, rx2, cnt2 = bfs(board, ry1, rx1, card2_y, card2_x)

    remove_card(board, card_pos, card_kind)
    backtracking(board, card_pos, orders, ry2, rx2, rmv_card_num + 1, ord_idx, count + cnt1 + cnt2)
    restore_card(board, card_pos, card_kind)

    # 한 쌍의 카드에서 두번째 카드를 먼저 지우는 경우이다.
    ry1, rx1, cnt1 = bfs(board, start_y, start_x, card2_y, card2_x)
    ry2, rx2, cnt2 = bfs(board, ry1, rx1, card1_y, card1_x)

    remove_card(board, card_pos, card_kind)
    backtracking(board, card_pos, orders, ry2, rx2, rmv_card_num + 1, ord_idx, count + cnt1 + cnt2)
    restore_card(board, card_pos, card_kind)


def solution(board, r, c):
    global answer
    # 종류 n인 카드가 저장된 위치를 card_pos[n][0, 1]로 찾을 수 있다.
    card_pos = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_pos[board[i][j]].append([i, j])
    
    # 순열을 사용하여 카드를 없애는 순서를 생성한다.
    orders = list(permutations(card_pos.keys()))
    
    for i in range(len(orders)):
        backtracking(board, card_pos, orders, r, c, 0, i, 0)

    return answer