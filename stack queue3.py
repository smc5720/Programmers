def solution(progresses, speeds):
    answer = []
    queue = []

    while progresses:
        day = int((99 - progresses[0]) / speeds[0]) + 1
        queue.append(day)
        progresses.pop(0)
        speeds.pop(0)
        
    while queue:
        cnt = 1
        val = queue.pop(0)
        while queue and val >= queue[0]:
            cnt += 1
            queue.pop(0)
        answer.append(cnt)

    return answer