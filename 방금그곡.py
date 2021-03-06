from collections import defaultdict

# '#'이 붙은 음을 하나로 바꾸는 함수
# (A# = a), (C# = c), (D# = d), (F# = f), (G# = g)
def change(s):
    arr = []
    for i in range(len(s) - 1):
        if s[i] == '#':
            continue
        if s[i + 1] == '#':
            if s[i] == 'A':
                arr.append('a')
            elif s[i] == 'C':
                arr.append('c')
            elif s[i] == 'D':
                arr.append('d')
            elif s[i] == 'F':
                arr.append('f')
            elif s[i] == 'G':
                arr.append('g')
        else:
            arr.append(s[i])
    if s[-1] != '#':
        arr.append(s[-1])
    return "".join(arr)

# 시간의 길이를 재는 함수
def time_length(start, end):
    start = int(start[:2]) * 60 + int(start[3:])
    end = int(end[:2]) * 60 + int(end[3:])
    return end - start


def solution(m, musicinfos):
    m = change(m)
    answer = '(None)'
    arr = []
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(',')
        musicinfos[i][3] = change(musicinfos[i][3])
    music_dict = defaultdict(list)
    idx = 0
    for i in musicinfos:
        idx += 1
        len_t = time_length(i[0], i[1])
        n = len_t // len(i[3])
        t = len_t % len(i[3])
        # 시간의 길이, 입력된 순서를 고려한다.
        music_dict[i[2]].append(len_t * (-1))
        music_dict[i[2]].append(idx)
        music_dict[i[2]].append(i[3] * n + i[3][:t])
        
    for key, val in music_dict.items():
        if m in val[2]:
            arr.append([val[0], val[1], key])
    if arr:
        arr.sort()
        answer = arr[0][2]
    return answer