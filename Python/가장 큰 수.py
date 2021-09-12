def solution(numbers):
    answer = ''
    arr = []

    for i in numbers:
        size = len(str(i))
        val = str(i) * 4
        arr.append([int(val[:4]) * (-1), size, i])

    arr.sort()

    for i in arr:
        answer += str(i[2])

    return str(int(answer))