def solution(answers):
    answer = []
    player = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    length = len(answers) - 1

    for i in range(0, 3):
        size = int(length / len(player[i])) + 1
        arr = player[i] * size
        player[i] = arr[:length + 1]
        
    arr = []
    idx = 0
    
    for pl in player:
        arr.append([0, idx + 1])
        for i in range(0, length + 1):
            if pl[i] == answers[i]:
                arr[idx][0] += 1
        idx += 1

    arr.sort()
    arr.reverse()

    high = arr[0][0]

    for i in range(0, len(arr)):
        if arr[i][0] == high:
            answer.append(arr[i][1])
        else:
            break

    answer.sort()

    return answer