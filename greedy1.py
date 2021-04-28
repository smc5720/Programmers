def solution(n, lost, reserve):    
    arr = []
    lost.sort()
    reserve.sort()
    tmp = lost[:]

    for i in tmp:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)

    for i in range (1, n + 1):
        arr.append(i)

    for i in lost:
        arr.remove(i)

    for i in reserve:
        if i - 1 not in arr:
            if i - 1 > 0:
                arr.append(i - 1)
        elif i not in arr:
            arr.append(i)
        elif i + 1 not in arr:
            if i + 1 <= n:
                arr.append(i + 1)
    print(arr)
    return len(arr)