def solution(priorities, location):
    answer = 0
    arr = priorities[:]
    arr.sort()
    rank = []

    for i in range(0, len(priorities)):
        rank.append(i)

    cnt = 1
    while priorities:
        if arr[-1] <= priorities[0]:
            arr.pop()
            priorities.pop(0)
            if location == rank[0]:
                answer = cnt
                break
            rank.pop(0)
            cnt += 1
        else:
            priorities.append(priorities.pop(0))
            rank.append(rank.pop(0))

    return answer