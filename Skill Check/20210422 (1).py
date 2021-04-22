import heapq

def solution(operations):
    heap = []
    answer = []

    for i in operations:
        if i[0] == "I":
            heapq.heappush(heap, int(i[2:]))
        else:
            if heap:
                if i[2] != "-":
                    heap = heapq.nlargest(len(heap), heap)[1:]
                    heapq.heapify(heap)
                else:
                    heapq.heappop(heap)

    if len(heap) > 0:
        heap = heapq.nlargest(len(heap), heap)
        answer.append(heap[0])
        answer.append(heap[-1])
    else:
        print("")
        answer.append(0)
        answer.append(0)

    return answer
