from itertools import permutations

# A와 B의 스펠링이 같은지 확인한다.
def spell_check(A, B):
    for i in range(len(A)):
        if B[i] == "*":
            continue
        if A[i] != B[i]:
            return False
    return True

# 현재 유저 아이디의 조합이 banned_id와 같은지 확인한다.
def check(now_set, banned_id):
    for i in range(len(now_set)):
        if len(now_set[i]) != len(banned_id[i]):
            return False
        if not spell_check(now_set[i], banned_id[i]):
            return False
    return True


def solution(user_id, banned_id):
    answer = set()
    # 유저 아이디로 만들 수 있는 모든 조합을 만든다.
    all_set = list(permutations(user_id, len(banned_id)))

    for i in all_set:
        # 해당 조합이 조건(banned_id)에 부합하는지 확인한다.
        if check(i, banned_id):
            tmp = list(i)
            tmp.sort()
            # 중복 방지를 위해 set을 사용했으며, list는 hashing이 안되기 때문에 str형으로 바꿔줬다.
            answer.add(str(tmp))

    return len(answer)