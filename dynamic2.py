def solution(triangle):
    answer = 0

    for i in range(0, len(triangle)):
        length = i + 1
        if length == 1:
            continue
        for j in range(0, length):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
        
        if i + 1 == len(triangle):
            for j in range(0, length):
                if answer < triangle[i][j]:
                    answer = triangle[i][j]

    return answer