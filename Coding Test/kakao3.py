def solution(n, k, cmd):
    arr = ["O"] * n
    trash = []
    tappend = trash.append
    tpop = trash.pop

    def move_down(n, idx, max_val):
        cnt = n
        tmp = idx
        while cnt > 0:
            tmp += 1
            if tmp >= max_val:
                return idx
            if arr[tmp] == "O":
                idx = tmp
                cnt -= 1
        return idx

    def move_up(n, idx):
        cnt = n
        tmp = idx
        while cnt > 0:
            tmp -= 1
            if tmp < 0:
                return idx
            if arr[tmp] == "O":
                idx = tmp
                cnt -= 1
        return idx

    for i in cmd:
        if i[0] == "D":
            k = move_down(int(i[2:]), k, len(arr))

        elif i[0] == "U":
            k = move_up(int(i[2:]), k)

        elif i[0] == "C":
            arr[k] = "X"
            trash.append(k)
            tmp = k
            k = move_down(1, k, len(arr))
            if k == tmp:
                k = move_up(1, tmp)

        else:
            if trash:
                arr[tpop()] = "O"

    return "".join(arr)