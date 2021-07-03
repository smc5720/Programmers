def solution(nums):
    answer = 0
    kind = set()
    N = len(nums)

    for i in nums:
        kind.add(i)
    
    answer = min(N // 2, len(kind))

    return answer