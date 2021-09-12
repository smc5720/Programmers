from collections import defaultdict

# 자카드 유사도를 반환한다.
def jaccard(A, B):
    intersec = 0
    unionsec = 0
    # 교집합의 원소 개수를 구하는 과정이다.
    for i in A.keys():
        intersec += min(A[i], B[i])
    # 합집합의 원소 개수를 구하는 과정이다.
    tmp = set(list(A.keys()) + list(B.keys()))
    for i in tmp:
        unionsec += max(A[i], B[i])
    return intersec / unionsec

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    # arr1, arr2에 각각 다중집합을 딕셔너리 형태로 저장한다.
    arr1 = defaultdict(int)
    arr2 = defaultdict(int)

    for i in range(0, len(str1) - 1):
        if 'a' <= str1[i] and str1[i] <= 'z' and 'a' <= str1[i+1] and str1[i+1] <= 'z':
            arr1[str1[i:i+2]] += 1
            
    for i in range(0, len(str2) - 1):
        if 'a' <= str2[i] and str2[i] <= 'z' and 'a' <= str2[i+1] and str2[i+1] <= 'z':
            arr2[str2[i:i+2]] += 1

    # 두 집합이 모두 공집합이라면 자카드 유사도는 1이다.
    # 따라서 1에 65536을 곱한 65536을 반환한다.
    if not arr1 and not arr2:
        return 65536
    else:
        return int(jaccard(arr1, arr2) * 65536)