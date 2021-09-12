from collections import defaultdict

def solution(record):
    answer = []
    arr = []
    user = defaultdict(list)

    for i in range(len(record)):
        tmp = record[i].split(" ")
        if tmp[0] != "Leave":
            user[tmp[1]] = tmp[2]
        arr.append([tmp[0], tmp[1]])
    
    for i in arr:
        if i[0] == "Enter":
            answer.append(user[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(user[i[1]] + "님이 나갔습니다.")
    
    return answer