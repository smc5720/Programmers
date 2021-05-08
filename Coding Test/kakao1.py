def solution(s):
    answer = []
    cnt = 0
    for i in range(0, len(s)):
        if cnt > 0:
            cnt -= 1
            continue
        if '0' <= s[i] and s[i] <= '9':
            answer.append(s[i])
        else:
            if s[i] == 'z':
                cnt = 3
                answer.append("0")

            elif s[i] == 'o':
                cnt = 2
                answer.append("1")

            elif s[i] == 't':
                if s[i + 1] == 'w':
                    cnt = 2
                    answer.append("2")

                else:
                    cnt = 4
                    answer.append("3")

            elif s[i] == 'f':
                if s[i + 1] == 'o':
                    cnt = 3
                    answer.append("4")

                else:
                    cnt = 3
                    answer.append("5")

            elif s[i] == 's':
                if s[i + 1] == 'i':
                    cnt = 2
                    answer.append("6")

                else:
                    cnt = 4
                    answer.append("7")

            elif s[i] == 'e':
                cnt = 4
                answer.append("8")

            elif s[i] == 'n':
                cnt = 3
                answer.append("9")

    return int(''.join(answer))