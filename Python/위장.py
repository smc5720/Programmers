def solution(clothes):
    answer = 1
    arr = {}

    for i in clothes:
        if i[1] in arr:
            arr[i[1]] += 1
        else:
            arr[i[1]] = 1

    for i in arr.values():
        answer *= i + 1
        
    answer -= 1
    return answer