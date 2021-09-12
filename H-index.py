def solution(citations):
    answer = 0
    citations.sort()
    length = len(citations)
    
    for i in range(length):
        if length - i <= citations[i]:
            answer = length - i
            break

    return answer