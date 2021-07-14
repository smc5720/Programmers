import heapq
# 우선순위 큐 구현을 위해 사용한다.

def dijkstra(graph, start):
    # start로 부터의 거리 값을 저장하기 위해 사용한다.
    distances = {node: float('inf') for node in graph}
    # 시작 값은 0이다.
    distances[start] = 0
    queue = []

    # 시작 노드부터 탐색 시작한다.
    heapq.heappush(queue, [distances[start], start])
    
    # queue에 남아있는 노드가 없으면 종료한다.
    while queue:
        # 탐색 할 노드와 거리를 가져온다.
        current_distance, current_destination = heapq.heappop(queue)
        # 기존에 있는 거리보다 길다면, 볼 필요도 없음
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            # 해당 노드를 거쳐 갈 때 거리
            distance = current_distance + new_distance

            # 현재 최소 거리보다 작으면 갱신한다.
            if distance < distances[new_destination]:  
                distances[new_destination] = distance
                # 다음 인접 거리를 계산하기 위해 큐에 삽입한다.
                heapq.heappush(queue, [distance, new_destination])
    
    return distances


def print_graph(graph):
    for key, val in graph.items():
        print(key, ":", val)


def solution(N, road, K):
    answer = 0
    graph = {}

    for i in range(1, N + 1):
        graph[i] = {}
        for j in range(1, N + 1):
            graph[i][j] = 500001

    for a, b, c in road:
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    # {1: 0, 2: 1, 3: 2, 4: 5, 5: 4, 6: 5}
    tmp = dijkstra(graph, 1)

    # value를 순회하며 K보다 낮은 값이 있다면 answer를 1 증가시킨다.
    for i in tmp.values():
        if i <= K:
            answer += 1

    return answer
