def solution(tickets):
    answer = []
    route = dict()

    for i in tickets:
        if i[0] in route:
            route[i[0]].append(i[1])
        else:
            route[i[0]] = [i[1]]
    
    for i in route.keys():
        route[i].sort()
    print(route)

    return answer
