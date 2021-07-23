def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def func(y, x, size):
        tmp = arr[y][x]
        for ny in range(y, y + size):
            for nx in range(x, x + size):
                if tmp != arr[ny][nx]:
                    nsize = size // 2
                    func(y, x, nsize)
                    func(y, x + nsize, nsize)
                    func(y + nsize, x, nsize)
                    func(y + nsize, x + nsize, nsize)
                    return
        answer[tmp] += 1

    func(0, 0, N)
    return answer