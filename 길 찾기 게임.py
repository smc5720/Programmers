# 재귀 함수를 사용할 경우, 아래 명령어로 재귀 함수의 제한을 풀어야 런타임 에러를 피할 수 있다.
import sys
sys.setrecursionlimit(10 ** 6)

# 재귀를 활용하여 트리를 구성한다.
class Tree:
    def __init__(self, data_list):
        # 현재 리스트에서 가장 level이 높은 노드가 root가 된다.
        tmp = max(data_list, key=lambda x : x[1])
        self.data = tmp[2]
        # root보다 x값이 작은 노드들은 왼쪽 자식 트리에 포함된다.
        left_list = list(filter(lambda x : x[0] < tmp[0], data_list))
        # root보다 x값이 큰 노드들은 오른쪽 자식 트리에 포함된다.
        right_list = list(filter(lambda x : x[0] > tmp[0], data_list))
        # 현재 노드의 왼쪽과 오른쪽 자식 트리를 선언한다.
        self.left = None
        self.right = None
        # 왼쪽 리스트가 존재한다면 리스트로 왼쪽 자식 트리를 만든다.
        if left_list:
            self.left = Tree(left_list)
        # 오른쪽 리스트가 존재한다면 리스트로 오른쪽 자식 트리를 만든다.
        if right_list:
            self.right = Tree(right_list)

        
def traversal(root, answer):
    # 현재 노드가 없는 노드라면 멈춘다.
    if root == None:
        return
    # 전위 순회 결과 배열은 answer[0]에 저장한다.
    answer[0].append(root.data)
    traversal(root.left, answer)
    traversal(root.right, answer)
    # 후위 순회 결과 배열은 answer[1]에 저장한다.
    answer[1].append(root.data)


def solution(nodeinfo):
    answer = [[], []]

    for i in range(1, len(nodeinfo) + 1):
        nodeinfo[i - 1].append(i)

    root = Tree(nodeinfo)
    traversal(root, answer)
    
    return answer