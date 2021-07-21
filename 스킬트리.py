def solution(skill, skill_trees):
    answer = 0

    for j in skill_trees:
        tmp = ""
        for i in j:
            if i in skill:
                tmp += i
        if skill.startswith(tmp):
            answer += 1

    return answer