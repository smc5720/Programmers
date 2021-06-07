import heapq

def time_cal(time, sec):
    hh = int(time[:2])
    mm = int(time[3:5])
    ss = int(time[6:8])
    sss = int(time[9:])

    if sec == "":
        sss -= 1
        ss += 1
        if sss < 0:
            sss = 999
            ss -= 1
        if ss >= 60:
            ss -= 60
            mm += 1
        if mm >= 60:
            mm -= 60
            hh += 1
        hh = str(hh)
        mm = str(mm)
        ss = str(ss)
        sss = str(sss)
        if len(hh) < 2:
            hh = "0" + hh
        if len(mm) < 2:
            mm = "0" + mm
        if len(ss) < 2:
            ss = "0" + ss
        while len(sss) < 3:
            sss = "0" + sss
        return hh + ":" + mm + ":" + ss + "." + sss

    sec = int(float(sec) * 1000) - 1
    sss -= sec
    while sss < 0:
        sss += 1000
        ss -= 1
    while ss < 0:
        ss += 60
        mm -= 1
    while mm < 0:
        mm += 60
        hh -= 1
    hh = str(hh)
    mm = str(mm)
    ss = str(ss)
    sss = str(sss)
    if len(hh) < 2:
        hh = "0" + hh
    if len(mm) < 2:
        mm = "0" + mm
    if len(ss) < 2:
        ss = "0" + ss
    while len(sss) < 3:
        sss = "0" + sss
    return hh + ":" + mm + ":" + ss + "." + sss

# A가 B보다 큰가? True / False
# A > B
def compare(A, B):
    hh1 = A[:2]
    mm1 = A[3:5]
    ss1 = A[6:8]
    sss1 = A[9:]
    hh2 = B[:2]
    mm2 = B[3:5]
    ss2 = B[6:8]
    sss2 = B[9:]
    tmp1 = int(hh1 + mm1 + ss1 + sss1)
    tmp2 = int(hh2 + mm2 + ss2 + sss2)
    return tmp1 > tmp2


def solution(lines):
    answer = 0

    for i in range(len(lines)):
        tmp = lines[i].split()
        lines[i] = [tmp[1], tmp[2][:-1]]
        # [시작시간, 끝나는시간 + 1]
        lines[i] = [time_cal(lines[i][0], lines[i][1]), time_cal(lines[i][0], "")]
    
    # lines를 정렬해준다. (시작시간이 모두 달라졌기 때문)
    lines.sort()
    queue = []

    tmp = ""
    for i in lines:
        # tmp는 시작하는 시간
        tmp = i[0]
        heapq.heappush(queue, i[1])
        # 시작하는 시간보다 끝나는 시간이 이르면 pop
        # tmp > queue[0]
        while queue and compare(tmp, queue[0]):
            heapq.heappop(queue)
        answer = max(answer, len(queue))

    return answer