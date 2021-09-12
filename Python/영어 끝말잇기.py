def solution(n, words):
    answer = [0, 0]
    word_set = set()
    cnt = 0
    pre_word = words[0]
    word_set.add(words[0])
    now_person = 1
    now_order = 1

    for i in words[1:]:
        cnt += 1
        now_person = cnt % n + 1
        now_order = cnt // n + 1

        if i[0] != pre_word[-1] or i in word_set:
            return [now_person, now_order]
        print(now_person, now_order, ":", i, word_set)
        word_set.add(i)
        pre_word = i

    return [0, 0]