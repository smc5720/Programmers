from itertools import permutations

def prime_number(num):
    if num < 2:
        return False
    x = int(num ** 0.5)
    for i in range(2, x + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = []
    for i in numbers:
        arr.append(int(i))
    
    tmp = []
    for i in range(1, len(arr) + 1):
        permute = permutations(arr, i)
        tmp += list(permute)

    arr = set()
    for i in tmp:
        n = ''
        for j in i:
            n += str(j)
        arr.add(int(n))
    
    print(arr)

    return answer