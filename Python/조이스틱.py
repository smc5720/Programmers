def find_idx(idx, name):
    idxR = idx + 1
    idxL = idx - 1

    while idxR < len(name):
        if name[idxR] != "A":
            break
        idxR += 1
    
    while idx != idxL:
        if idxL < 0:
            idxL += len(name)
        if name[idxL] != "A":
            break
        idxL -= 1

    if idxR >= len(name):
        idxR = 100

    return idxL, idxR


def solution(name):
    answer = 0
    
    for idx in range(0, len(name)):
        i = name[idx]
        
        if i == "A":
            continue

        tmpA = ord(i) - ord('A')
        tmpZ = ord('Z') - ord(i) + 1
        #print(tmpA, tmpZ)

        if tmpA < tmpZ:
            answer += tmpA
        else:
            answer += tmpZ
    #print("answer:", answer)

    st = "A" * len(name)
    idx = 0
    name = name[:idx] + "A" + name[idx + 1:]

    while st != name:
        tmpL, tmpR = find_idx(idx, name)
        #print(idx, tmpL, tmpR)
        movR = tmpR - idx
        if idx > tmpL:
            movL = idx - tmpL
        else:
            movL = idx + len(name) - tmpL
        #print(idx, movL, movR)

        if movR <= movL:
            #print("right:", movR)
            answer += movR
            idx = tmpR
        else:
            #print("left:", movL)
            answer += movL
            idx = tmpL
        #print(idx)
        name = name[:idx] + "A" + name[idx + 1:]
        #print(name)

    return answer