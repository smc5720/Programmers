from collections import defaultdict

def solution(n, edge):
    answer = 0
    v_dict = defaultdict(list)
    visited = [False] * (n + 1)
    visited[1] = True
    queue = [1]
    arr = []
    
    for i in edge:
        v_dict[i[0]].append(i[1])
    
    def bfs():
        cnt = 0
        while queue:
            cnt += 1
            tmp = queue.pop(0)
            for i in v_dict[tmp]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
                    arr.append(cnt)
    bfs

    answer = arr.count(max(arr))
    return answer