def root(num):
    return int(num ** 0.5)

def solution(brown, yellow):
    val = root(yellow)

    for i in range(1, val + 1):
        if yellow % i == 0:
            width = yellow / i
            size = width * 2 + i * 2 + 4
            if size == brown:
                width += 2
                height = i + 2
                answer = [width, height]

    return answer