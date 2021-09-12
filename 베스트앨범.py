from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_dict = defaultdict(lambda: 0)
    total_list = defaultdict(lambda: [])

    for i in range(0, len(genres)):
        genre_dict[genres[i]] += plays[i]
        total_list[genres[i]].append((plays[i], i))

    genre_dict = sorted(genre_dict.items(), key=lambda x:x[1], reverse=True)

    for i in total_list.keys():
        total_list[i] = sorted(total_list[i], key=lambda x:x[0], reverse=True)

    for i in genre_dict:
        if len(total_list[i[0]]) > 1:
            answer.append(total_list[i[0]][0][1])
            answer.append(total_list[i[0]][1][1])
        else:
            answer.append(total_list[i[0]][0][1])

    return answer
