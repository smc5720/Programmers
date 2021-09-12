def solution(word, pages):
    answer = 0
    word = word.lower()
    # { 'a.com': 0, 'b.com': 1, 'c.com': 2, ... }
    web_dict = {}
    web_index = 0
    # 현재 페이지의 기본 점수를 저장한다.
    basic_score = [0 for _ in range(len(pages))]
    # 현재 페이지가 공유하는 링크들을 저장한다.
    sharing_link = [[] for _ in range(len(pages))]
    
    for i in pages:
        # 현재 페이지의 인덱스를 web_dict에 등록한다.
        now_link = i.split("<meta property=\"og:url\" content=")[1]
        now_link = now_link.split("/>")[0]
        now_link = now_link[len("https://") + 1:-1]
        web_dict[now_link] = web_index

        # 현재 페이지가 공유하는 링크들을 sharing_link에 저장한다.
        tmp = i.split("<a href=")
        if len(tmp) > 1:
            for j in range(1, len(tmp)):
                tmp_s = tmp[j]
                tmp_s = tmp_s.split(">")[0]
                tmp_s = tmp_s[len("https://") + 1:-1]
                sharing_link[web_index].append(tmp_s)
        
        # 본문 내용을 추려낸다.
        tmp = " ".join(i.split())
        tmp = tmp.split("<body>")[1]
        tmp = tmp.split("</body>")[0]
        tmp = tmp.split("<")
        tmp_arr = []
        for j in tmp:
            if ">" in j:
                tmp_s = j.split(">")
                tmp_arr += tmp_s
            else:
                tmp_arr.append(j)
        tmp = []
        for j in tmp_arr:
            if len(j) < 1:
                continue
            if j.startswith("a href"):
                continue
            if j.startswith("/a"):
                continue
            tmp_s = j.split()
            tmp += tmp_s
        tmp_arr = []
        for j in tmp:
            tmp_s = ""
            for k in j:
                if "a" <= k <= "z" or "A" <= k <= "Z":
                    tmp_s += k.lower()
                else:
                    if tmp_s != "":
                        tmp_arr.append(tmp_s)
                        tmp_s = ""
            if tmp_s != "":
                        tmp_arr.append(tmp_s)
                        tmp_s = ""
        for j in tmp_arr:
            if j == word:
                basic_score[web_index] += 1
        web_index += 1
    
    matching_score = basic_score[:]

    for i in range(web_index):
        # 만약 공유 중인 링크가 있다면
        if len(sharing_link[i]) > 0:
            # 링크 점수 = 기본 점수 / 공유 링크 수
            link_score = basic_score[i] / len(sharing_link[i])
            for j in sharing_link[i]:
                if j in web_dict:
                    # 링크 점수를 공유 중인 링크의 기본 점수에 더해준다.
                    matching_score[web_dict[j]] += link_score

    # 매칭 점수가 가장 높은 페이지의 index를 구한다.
    max_score = 0
    for i in range(web_index):
        if max_score < matching_score[i]:
            answer = i
            max_score = matching_score[i]

    return answer