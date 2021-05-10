answer = 0

def solution(begin, target, words):
    visited = [False] * len(words)
    word_len = len(words[0])

    def check_word(a, b):
        cnt = word_len
        for i in range(0, word_len):
            if a[i] == b[i]:
                cnt -= 1
        return cnt

    def dfs(i, route):
        global answer
        if words[i] == target:
            if answer > 0:
                answer = min(answer, route)
            else:
                answer = route
                
        for j in range(0, len(words)):
            if visited[j] == True:
                continue
            if check_word(words[i], words[j]) == 1:
                visited[j] = True
                dfs(j, route + 1)
                visited[j] = False

    idx = 0
    for i in words:
        cnt = check_word(i, begin)
        if cnt == 1:
            visited[idx] = True
            route = 1
            dfs(idx, route)
            visited[idx] = False
        idx += 1

    return answer