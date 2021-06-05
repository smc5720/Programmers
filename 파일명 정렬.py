def solution(files):
    answer = []
    arr = []

    for s in files:
        # head를 분리한다.
        head = ""
        for c in s:
            if c.isdigit():
                break
            head += c
        
        # number를 분리한다.
        num = ""
        for n in s[len(head):]:
            if not n.isdigit():
                break
            num += n
        
        arr.append([head, num, s])
    
    # 정렬 기준에 따라 정렬한다.
    s_list = sorted(arr, key=lambda x: (x[0].lower(), int(x[1])))

    for i in s_list:
        answer.append(i[2])

    return answer