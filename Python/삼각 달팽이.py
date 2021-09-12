def print_arr(arr):
    print("--print array--")
    for i in arr:
        print(i)


def solution(n):
    answer = []
    arr = [[0 for _ in range(1, i + 1)] for i in range(1, n + 1)]

    # 방향을 설정한다.
    DOWN, RIGHT, UP = n % 3, (n - 1) % 3, (n - 2) % 3
    # 현 위치를 저장한다.
    now_y, now_x = 0, 0

    cnt = 1

    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            # 아래로 움직여야 할 상태라면
            if i % 3 == DOWN:
                arr[now_y][now_x] = cnt
                cnt += 1
                if j < i:
                    # 현 위치가 마지막 칸이 아니라면 아래로 한 칸 움직인다.
                    now_y += 1
                else:
                    # 현 위치가 마지막 칸이라면 오른쪽으로 한 칸 움직인다.
                    now_x += 1
            # 오른쪽으로 움직여야 할 상태라면
            elif i % 3 == RIGHT:
                arr[now_y][now_x] = cnt
                cnt += 1
                if j < i:
                    # 현 위치가 마지막 칸이 아니라면 오른쪽으로 한 칸 움직인다.
                    now_x += 1
                else:
                    # 현 위치가 마지막 칸이라면 ↖쪽으로 한 칸 움직인다.
                    now_y -= 1
                    now_x -= 1
            # ↖쪽으로 움직여야 할 상태라면
            elif i % 3 == UP:
                arr[now_y][now_x] = cnt
                cnt += 1
                if j < i:
                    # 현 위치가 마지막 칸이 아니라면 ↖쪽으로 한 칸 움직인다.
                    now_y -= 1
                    now_x -= 1
                else:
                    # 현 위치가 마지막 칸이라면 아래쪽으로 한 칸 움직인다.
                    now_y += 1
    
    for i in arr:
        answer += i

    return answer