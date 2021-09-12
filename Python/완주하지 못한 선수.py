def solution(participant, completion):
    answer = ''
    player = {}

    for i in participant:
        if i in player:
            player[i] += 1
        else:
            player[i] = 1

    for i in completion:
        player[i] -= 1

    for key, value in player.items():
        if value > 0:
            answer = key
            break

    return answer