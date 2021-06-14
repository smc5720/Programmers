import heapq

# 다익스트라 알고리즘이다.
def dijkstra(graph, start):
    # 처음에는 모두 갈 수 없다고 표기한다.
    distances = {node: float('inf') for node in graph.keys()}
    # 출발지는 0이다.
    distances[start] = 0
    # 이동할 경로를 저장하는 queue이다.
    queue = []
    # 최소 힙을 사용하여 가까운 거리부터 이동하도록 설정한다.
    heapq.heappush(queue, [distances[start], start])

    while queue:
        # 현재까지의 최소 비용과 목적지를 의미한다. 
        current_dist, current_destination = heapq.heappop(queue)

        # 만약 현 경로의 최소 비용이 목적지에 저장된 최소 비용보다 크다면 더 진행할 이유가 없다.
        if current_dist > distances[current_destination]:
            continue

        # graph에는 {목적지: 비용}의 형태로 값을 저장했다.
        for new_destination, new_dist in graph[current_destination].items():
            # 현재까지의 최소 비용과 앞으로 갈 목적지까지의 비용을 더한다.
            dist = current_dist + new_dist
            # 이 값이 이동하려는 목적지의 최소 비용보다 작다면
            if dist < distances[new_destination]:
                # 해당 목적지의 최소 비용을 초기화하고
                distances[new_destination] = dist
                # 해당 경로로 이동하도록 queue에 경로를 넣는다.
                heapq.heappush(queue, [dist, new_destination])

    return distances


def solution(n, s, a, b, fares):
    answer = float('inf')
    # graph는 node끼리의 연결 관계를 저장한다.
    graph = {(node + 1): {} for node in range(n)}

    # 양방향 그래프이므로 둘 다 등록해준다.
    for start, end, fee in fares:
        graph[start][end] = fee
        graph[end][start] = fee

    # i는 경유지로, 점화식은 "최소비용(출발지 ~ i) + 최소비용(i ~ A) + 최소비용(i ~ B)"이다. 
    for i in range(1, n + 1):
        tmp = dijkstra(graph, s)[i] + dijkstra(graph, i)[a] + dijkstra(graph, i)[b]
        answer = min(answer, tmp)

    return answer