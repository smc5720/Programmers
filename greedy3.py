def solution(number, k):
    answer = str(number)
    cnt = 0
    st = []

    for i in answer:
        if not st:
            st.append(i)
        else:
            if st[-1] < i:
                st.pop()
        
    return answer