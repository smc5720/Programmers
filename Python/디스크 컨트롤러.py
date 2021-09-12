import heapq

def solution(jobs):
    answer = 0
    size = len(jobs)
    heap = []
    jobs.sort()

    timer = 0

    while jobs or heap:
        while jobs and timer >= jobs[0][0]:
            heapq.heappush(heap, (jobs[0][1], jobs[0][0]))
            jobs.pop(0)
        #print(timer, heap)

        if len(heap) > 0:
            timer += heap[0][0]
            answer += (timer - heap[0][1])
            heapq.heappop(heap)
        else:
            timer += 1
    #print(timer, heap)
    return int(answer / size)