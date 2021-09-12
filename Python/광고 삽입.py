def sec_to_time(sec):
    hh = sec // (60 * 60)
    sec -= hh * (60 * 60)
    mm = sec // 60
    sec -= mm * 60
    ss = sec
    hh = str(hh)
    if len(hh) < 2:
        hh = "0" + hh
    mm = str(mm)
    if len(mm) < 2:
        mm = "0" + mm
    ss = str(ss)
    if len(ss) < 2:
        ss = "0" + ss
    return str(hh) + ":" + str(mm) + ":" + str(ss)


def time_to_sec(time):
    hh = int(time[:2])
    mm = int(time[3:5])
    ss = int(time[6:])
    return hh * 3600 + mm * 60 + ss


def solution(play_time, adv_time, logs):
    answer = 0
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    # 이런 미친 방법이 정답일거라곤 생각하지 못했다.
    # 초당 1개의 배열을 생성하여 누적 시청자 수를 계산한다.
    all_time = [0 for _ in range(play_time + 1)]
    
    for i in logs:
        # 로그를 시작 시간과 끝 시간으로 분리한다.
        start, end = i.split("-")
        start = time_to_sec(start)
        end = time_to_sec(end)
        # 시작 시간에는 1을 더해준다.
        all_time[start] += 1
        # 끝 시간에는 1을 빼준다.
        all_time[end] -= 1
    
    for i in range(1, play_time + 1):
        # 각 시간에 몇 명이 보고 있었는지 계산해준다.
        all_time[i] = all_time[i] + all_time[i-1]

    for i in range(1, play_time + 1):
        # 누적 시청자 수를 계산해준다.
        all_time[i] = all_time[i] + all_time[i-1]

    max_val = 0
    for i in range(0, play_time + 1):
        # 계산한 시간으로부터 누적 시청자 수가 가장 많았던 구간을 탐색한다.
        start_point = i - adv_time
        if start_point < 0:
            start_point = 0
        tmp = all_time[i] - all_time[i - adv_time]
        # start_point ~ start_point + adv_time에 가장 많은 시청자가 존재했음을 나타낸다.
        if max_val < tmp:
            answer = start_point
            max_val = tmp

    if answer != 0:
        answer += 1

    return sec_to_time(answer)