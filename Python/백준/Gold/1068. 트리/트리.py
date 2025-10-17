
import sys
input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

# 트리 구조 구성 (인접 리스트)
tree = [[] for _ in range(N)]
root = -1

for child, p in enumerate(parent):
    if p == -1:
        root = child  # 루트 노드 기록
    else:
        tree[p].append(child)

# 삭제된 노드는 방문하지 않도록 처리
def dfs(node):
    # 삭제된 노드는 탐색하지 않음
    if node == remove_node:
        return 0
    # 리프 노드 여부 판단
    if len(tree[node]) == 0:
        return 1

    # 자식 탐색
    leaf_count = 0
    for child in tree[node]:
        if child == remove_node:
            continue
        leaf_count += dfs(child)

    # 자식이 모두 삭제된 경우, 자신이 리프가 됨
    if leaf_count == 0:
        return 1
    return leaf_count

# 루트 자체가 삭제된 경우
if root == remove_node:
    print(0)
else:
    print(dfs(root))
