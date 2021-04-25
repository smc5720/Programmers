import heapq

def solution(operations):
    answer = []
    heap = []

    for i in operations:
        if i[0] == "I":
            heapq.heappush(heap, int(i[2:]))
        else:
            if heap:
                if i[2] == "-":
                    heapq.heappop(heap)
                else:
                    heap.sort()
                    heap.pop()
                    heapq.heapify(heap)
    
    if len(heap) > 0:
        heap.sort()
        answer.append(heap[-1])
        answer.append(heap[0])
    else:
        answer.append(0)
        answer.append(0)

    return answer