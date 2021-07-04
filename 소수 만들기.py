from itertools import combinations
import math


def print_prime(arr):
    for i in range(len(arr)):
        print(i, ":", arr[i])


def solution(nums):
    answer = 0
    num_set = []
    tmp = list(combinations(nums, 3))

    for j in tmp:
        num_set.append(sum(j))
    
    max_num = max(num_set)
    prime_arr = [False, False] + [True] * (max_num - 1)

    for i in range(2, int(math.sqrt(max_num)) + 1):
        if prime_arr[i]:
            for j in range(2 * i, max_num + 1, i):
                prime_arr[j] = False
    
    for i in num_set:
        if prime_arr[i]:
            answer += 1

    return answer