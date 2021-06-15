# 보가 설치될 수 있는지 확인한다.
def check_insert_bo(y, x_left, pillar, bo, n):
    # 높이가 0이거나 x_left가 한계점일 경우
    if y == 0 or x_left == n:
        return False
    # 보의 왼쪽 또는 오른쪽 끝에 기둥이 존재하는 경우
    if pillar[y - 1][x_left] or pillar[y - 1][x_left + 1]:
        return True
    # 보의 양쪽 끝에 동시에 보가 존재하는 경우
    if bo[y][x_left - 1] and bo[y][x_left + 1]:
        return True
    return False

# 기둥이 설치될 수 있는지 확인한다.
def check_insert_pillar(y_low, x, pillar, bo, n):
    # 높이가 한계점일 경우
    if y_low == n:
        return False
    # 높이가 0이거나, 바로 아래에 기둥이 존재하는 경우
    if y_low == 0 or pillar[y_low - 1][x]:
        return True
    # 바로 밑에 왼쪽으로 보가 존재하는 경우
    if x > 0 and bo[y_low][x - 1]:
        return True
    # 바로 밑에 오른쪽으로 보가 존재하는 경우
    if x < n and bo[y_low][x]:
        return True
    return False

# 기둥이 삭제될 수 있는지 확인한다.
def check_delete_pillar(y_low, x, pillar, bo, n):
    if pillar[y_low][x] == False:
        return False
    # 일단 기둥과 기둥과 연결되었던 것들을 삭제해본다.
    pillar[y_low][x] = False
    # 현재 기둥 위에 다른 기둥이 존재한다면 해당 기둥이 설치될 수 있는지 확인한다.
    if pillar[y_low + 1][x] and not check_insert_pillar(y_low + 1, x, pillar, bo, n):
        pillar[y_low][x] = True
        return False
    # 현재 기둥 왼쪽 위에 다른 보가 존재한다면 해당 보가 설치될 수 있는지 확인한다.
    if x - 1 >= 0 and bo[y_low + 1][x - 1] and not check_insert_bo(y_low + 1, x - 1, pillar, bo, n):
        pillar[y_low][x] = True
        return False
    # 현재 기둥 오른쪽 위에 다른 보가 존재한다면 해당 보가 설치될 수 있는지 확인한다.
    if bo[y_low + 1][x] and not check_insert_bo(y_low + 1, x, pillar, bo, n):
        pillar[y_low][x] = True
        return False
    return True
    
# 보가 삭제될 수 있는지 확인한다.
def check_delete_bo(y, x_left, pillar, bo, n):
    if bo[y][x_left] == False:
        return False
    # 일단 보를 삭제해본다.
    bo[y][x_left] = False
    #현재 보 왼쪽 위에 기둥이 존재한다면 해당 기둥이 설치될 수 있는지 확인한다.
    if pillar[y][x_left] and not check_insert_pillar(y, x_left, pillar, bo, n):
        bo[y][x_left] = True
        return False
    #현재 보 오른쪽 위에 기둥이 존재한다면 해당 기둥이 설치될 수 있는지 확인한다.
    if pillar[y][x_left + 1] and not check_insert_pillar(y, x_left + 1, pillar, bo, n):
        bo[y][x_left] = True
        return False
    # 현재 보 왼쪽에 다른 보가 존재한다면 해당 보가 설치될 수 있는지 확인한다.
    if x_left - 1 >= 0 and bo[y][x_left - 1] and not check_insert_bo(y, x_left - 1, pillar, bo, n):
        bo[y][x_left] = True
        return False
    # 현재 보 오른쪽에 다른 보가 존재한다면 해당 보가 설치될 수 있는지 확인한다.
    if bo[y][x_left + 1] and not check_insert_bo(y, x_left + 1, pillar, bo, n):
        bo[y][x_left] = True
        return False
    return True


def solution(n, build_frame):
    answer = []
    # 기둥은 pillar[y_low][x] = True 형태로 저장된다.
    pillar = [[False] * (n + 1) for _ in range(n + 1)]
    # 보는 bo[y][x_left] 형태로 저장된다.
    bo = [[False] * (n + 1) for _ in range(n + 1)]

    for x, y, a, b in build_frame:
        # 기둥이라면
        if a == 0:
            # 설치한다면
            if b == 1:
                if check_insert_pillar(y, x, pillar, bo, n):
                    print(y, x, "에 기둥 설치")
                    pillar[y][x] = True
            # 삭제한다면
            else:
                if check_delete_pillar(y, x, pillar, bo, n):
                    print(y, x, "에 기둥 삭제")
                    pillar[y][x] = False
            
        # 보라면
        if a == 1:
            # 설치한다면
            if b == 1:
                if check_insert_bo(y, x, pillar, bo, n):
                    print(y, x, "에 보 설치")
                    bo[y][x] = True
            # 삭제한다면
            else:
                if check_delete_bo(y, x, pillar, bo, n):
                    print(y, x, "에 보 삭제")
                    bo[y][x] = False

    for y in range(n + 1):
        for x in range(n + 1):
            if pillar[y][x]:
                answer.append([x, y, 0])
            if bo[y][x]:
                answer.append([x, y, 1])

    answer.sort()

    return answer