def solution(number, k):
    answer = str(number)
    cnt = 0
    st = []

    for i in answer:
        while st and st[-1] < i and cnt < k:
            st.pop()
            cnt += 1
        st.append(i)

    answer = ''.join(st)

    if cnt != k:
        answer = answer[:-(k - cnt)]

    return str(int(answer))