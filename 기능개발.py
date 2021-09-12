def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = [0] * bridge_length
    w = 0

    while que:
        answer += 1
        w -= que.pop(0)
        if truck_weights:
            if w + truck_weights[0] <= weight:
                w += truck_weights[0]
                que.append(truck_weights.pop(0))
            else:
                que.append(0)

    return answer