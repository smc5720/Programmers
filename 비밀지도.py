def solution(n, arr1, arr2):
    answer = []
    map_one = []
    map_two = []

    for i in arr1:
        map_one.append(str(bin(i)[2:]))
    for i in arr2:
        map_two.append(str(bin(i)[2:]))

    for i in range(n):
        if len(map_one[i]) < n:
            map_one[i] = "0" * (n - len(map_one[i])) + map_one[i]
        if len(map_two[i]) < n:
            map_two[i] = "0" * (n - len(map_two[i])) + map_two[i]
    
    for i in range(n):
        arr = []
        for j in range(n):
            if map_one[i][j] == "1" or map_two[i][j] == "1":
                arr.append("#")
            else:
                arr.append(" ")
        answer.append("".join(arr))

    return answer