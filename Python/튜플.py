def solution(s):
    answer = []
    arr = []
    # s는 문자열로 되어있으므로 리스트 형태로 바꾼다.
    s = s.split("},")
    for i in s:
        tmp = []
        tmp_s = ""
        for j in i:
            if "0" <= j and j <= "9":
                tmp_s += j
            if j == ",":
                tmp.append(int(tmp_s))
                tmp_s = ""
        tmp.append(int(tmp_s))
        # s   = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
        # arr =  [[2],[2,1],[2,1,3],[2,1,3,4]]
        arr.append(tmp)

    # 리스트의 길이를 기준으로 정렬한다.
    arr.sort(key=len)
    
    # 순서대로 리스트에 값을 넣어준다.
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer