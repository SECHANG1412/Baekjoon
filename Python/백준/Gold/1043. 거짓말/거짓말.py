import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# find: 루트 찾기 (경로 압축)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# union: 두 집합 합치기
def union(a, b):
    a_root, b_root = find(a), find(b)
    if a_root != b_root:
        parent[b_root] = a_root

# 입력 처리
N, M = map(int, input().split())
truth = list(map(int, input().split()))
T = truth[0]          # 진실을 아는 사람 수
truth_people = truth[1:] if T > 0 else []

parent = [i for i in range(N + 1)]
parties = []

# 파티 정보 입력
for _ in range(M):
    people = list(map(int, input().split()))[1:]  # 첫 숫자는 인원 수
    parties.append(people)

    # 같은 파티에 있는 사람들끼리 union
    for i in range(len(people) - 1):
        union(people[i], people[i + 1])

# 진실을 아는 사람들의 루트 집합
truth_roots = set(find(p) for p in truth_people)

# 거짓말 가능한 파티 개수 계산
cnt = 0
for people in parties:
    # 해당 파티의 대표 루트가 truth_roots에 속하면 → 진실 퍼짐
    if all(find(p) not in truth_roots for p in people):
        cnt += 1

print(cnt)