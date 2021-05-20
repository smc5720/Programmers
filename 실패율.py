from collections import defaultdict

def solution(N, stages):
    answer = []
    stage_dict = defaultdict(int)
    arr = []
    people = len(stages)

    for i in stages:
        if i <= N:
            stage_dict[i] += 1
    
    for i in range(1, N + 2):
        arr.append([people, i])
        people -= stage_dict[i]

    for i in range(0, N):
        if arr[i][0] != 0:
            arr[i][0] = -1 * (arr[i][0] - arr[i + 1][0]) / arr[i][0]
        else:
            arr[i][0] = 0
    
    arr.pop()
    arr.sort()

    for i in arr:
        answer.append(i[1])

    return answer