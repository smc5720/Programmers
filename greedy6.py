def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001

    for i in routes:
        if camera < i[0]:
            answer += 1
            camera = i[1]

    return answer
