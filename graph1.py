from collections import deque

def solution(n, edge):
    routes = dict()
    for a, b in edge:
        routes.setdefault(a, []).append(b)
        routes.setdefault(b, []).append(a)
    
    q = deque([[1, 0]])
    check = [-1] * (n + 1)

    while q:
        idx, depth = q.popleft()
        check[idx] = depth
        for i in routes[idx]:
            if check[i] == -1:
                check[i] = 0
                q.append([i, depth+1])

    return check.count(max(check))