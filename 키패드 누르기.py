def solution(numbers, hand):
    answer = []
    keyboard = [(3, 1),
                (0, 0), (0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
                (2, 0), (2, 1), (2, 2),
                (3, 0), (3, 2)]
    
    hand_L = 10
    hand_R = 11

    for i in numbers:
        if i in [1, 4, 7]:
            hand_L = i
            answer.append('L')

        if i in [3, 6, 9]:
            hand_R = i
            answer.append('R')

        if i in [2, 5, 8, 0]:
            distance_L = abs(keyboard[hand_L][0] - keyboard[i][0]) + abs(keyboard[hand_L][1] - keyboard[i][1])
            distance_R = abs(keyboard[hand_R][0] - keyboard[i][0]) + abs(keyboard[hand_R][1] - keyboard[i][1])
            if distance_L < distance_R:
                hand_L = i
                answer.append('L')
            elif distance_L > distance_R:
                hand_R = i
                answer.append('R')
            else:
                if hand == "left":
                    hand_L = i
                    answer.append('L')
                else:
                    hand_R = i
                    answer.append('R')
    
    return "".join(answer)