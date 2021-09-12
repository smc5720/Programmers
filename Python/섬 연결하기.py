def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    parent = [0] * n

    for i in range(0, n):
        parent[i] = i

    def get_parent(num):
        if num == parent[num]:
            return num
        else:
            return get_parent(parent[num])

    def set_parent(a, b):
        pa = get_parent(a)
        pb = get_parent(b)
        
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb
    
    for i in costs:
        if get_parent(i[0]) != get_parent(i[1]):
            set_parent(i[0], i[1])
            answer += i[2]

    return answer