def solution(gems):
    answer = []
    shortest = len(gems) + 1
    
    jewel = set(gems)
    # defaultdict는 len이 적용되지 않는다.
    contained = {}
    
    # 투포인터를 활용하여 문제를 해결한다.
    start = 0
    end = 0
    
    while end < len(gems):
        if gems[end] not in contained:
            contained[gems[end]] = 1
        else:
            contained[gems[end]] += 1
        end += 1

        # contained의 보석 종류의 개수가 전체 보석 종류의 개수와 같다면
        if len(contained) == len(jewel):
            while start < end:
                # start에 해당하는 보석이 2개 이상이라면
                if contained[gems[start]] > 1:
                    # 해당 보석을 버리고 start를 1 더해준다.
                    contained[gems[start]] -= 1
                    start += 1
                # end는 이미 한칸 앞으로 와있는 상태이다.
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break

    return answer