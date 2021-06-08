import heapq

# 시간을 빼준다.
def time_minus(time, t):
    hh = time[:2]
    mm = time[3:]
    mm = int(mm) - t
    hh = int(hh)
    while mm < 0:
        mm += 60
        hh -= 1
    hh = str(hh)
    mm = str(mm)
    if len(hh) < 2:
        hh = "0" + hh
    if len(mm) < 2:
        mm = "0" + mm
    return hh + ":" + mm

# 시간을 더해준다.
def time_add(time, t):
    hh = time[:2]
    mm = time[3:]
    mm = int(mm) + int(t)
    hh = int(hh)
    hh += mm // 60
    mm %= 60
    hh = str(hh)
    mm = str(mm)
    if len(hh) < 2:
        hh = "0" + hh
    if len(mm) < 2:
        mm = "0" + mm
    return hh + ":" + mm

# A <= B인가?
def time_compare(A, B):
    hh_a = A[:2]
    mm_a = A[3:]
    hh_b = B[:2]
    mm_b = B[3:]
    tmp_a = int(hh_a + mm_a)
    tmp_b = int(hh_b + mm_b)
    return tmp_a <= tmp_b


def solution(n, t, m, timetable):
    answer = ''
    # timetable을 최소힙 형태로 바꿔준다.
    heapq.heapify(timetable)
    for i in range(n):
        bus_time = "09:00"
        # 버스 시간을 배차 간격에 맞게 계산한다.
        bus_time = time_add(bus_time, i * t)
        cnt = 0
        # tmp는 콘이 셔틀을 타야할 시간을 의미한다.
        tmp = bus_time
        while cnt < m and timetable and time_compare(timetable[0], bus_time):
            cnt += 1
            # 셔틀의 가장 마지막 자리에 앉을 사람보다 1분 먼저오면 가장 마지막에 셔틀을 탈 수 있다.
            if cnt == m:
                tmp = time_minus(timetable[0], 1)
            heapq.heappop(timetable)
        if i + 1 == n:
            answer = tmp

    return answer