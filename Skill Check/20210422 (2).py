def solution(tickets):
    answer = []
    route = dict()

    for i in tickets:
        if i[0] in route:
            route[i[0]].append(i[1])
        else:
            route[i[0]] = [i[1]]
    
    for i in route.keys():
        route[i].sort(reverse=True)
        
    start = ["ICN"]

    while start:
        stack = start[-1]
        if stack not in route or len(route[stack]) == 0:
            answer.append(start.pop())
        else:
            start.append(route[stack].pop())

    return answer[::-1]
