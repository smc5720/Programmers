def solution(people, limit):
    answer = 0
    people.sort()
    first = 0
    second = len(people) - 1

    while first <= second:
        if people[second] <= limit / 2:
            answer += int((second - first + 2) / 2) 
            break
        else:
            answer += 1
            if people[second] + people[first] <= limit:
                first += 1
            second -= 1

    return answer