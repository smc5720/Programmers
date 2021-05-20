from collections import defaultdict

def solution(N, stages):
    answer = []
    stage_dict = defaultdict(int)
    arr = []

    for i in stages:
        if i <= N:
            stage_dict[i] += 1
    
    for i in range(1, N + 1):
        arr.append([len(stages), i])

    print(stage_dict, arr)
    return answer