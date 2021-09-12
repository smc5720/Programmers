from collections import defaultdict
from collections import deque

def solution(msg):
    answer = []
    zip_dict = defaultdict(int)

    # 대문자 사전을 미리 만들어준다.
    for i in range(1, 27):
        zip_dict[chr(64 + i)] = i

    # 추가 단어를 저장하기 위한 idx
    idx = 27
    msg = deque(msg)

    # popleft가 아닌 pop을 이용하기 위한 reverse
    # 그러나 찾아보니 deque는 pop과 popleft, append와 appendleft의 시간복잡도가 같다.
    msg.reverse()
    
    while msg:
        tmp = msg[-1] 
        val = 0
        # 사전에 등록하는 과정이다.
        while zip_dict[tmp] != 0:
            val = zip_dict[tmp]
            msg.pop()
            if not msg:
                break
            tmp += msg[-1]
        zip_dict[tmp] = idx
        idx += 1
        answer.append(val)

    return answer