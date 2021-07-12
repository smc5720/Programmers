def solution(n,a,b):
    answer = 1

    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    # 2와 3 같은 경우, 끝나면 안되는데 끝나는 경우가 있다.
    # 이를 방지하기 위해 small이 홀수여야 한다는 조건을 추가한다.
    while small + 1 != big or small % 2 == 0:
        answer += 1
        small = (small + 1) // 2
        big = (big + 1) // 2
    
    return answer