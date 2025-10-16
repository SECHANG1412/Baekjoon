import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
build_time = [0] * (N + 1)

# 1. 입력 처리
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    build_time[i] = data[0]           # 해당 건물 짓는 데 걸리는 시간
    for prereq in data[1:-1]:         # -1은 -1(끝 표시)이므로 제외
        graph[prereq].append(i)       # 선행 건물 → 현재 건물
        indegree[i] += 1              # 진입 차수 증가

# 2. 위상 정렬용 큐 초기화
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:  # 선행 건물 없는 경우
        queue.append(i)

# 3. 누적 결과(건물 완성 시간)
result = build_time[:]  # 자기 자신 짓는 시간 포함

# 4. 위상 정렬 수행 (BFS)
while queue:
    now = queue.popleft()

    for nxt in graph[now]:
        indegree[nxt] -= 1
        # 현재 건물 완공 시간 + 다음 건물 짓는 시간 비교 → 최댓값 유지
        result[nxt] = max(result[nxt], result[now] + build_time[nxt])
        if indegree[nxt] == 0:
            queue.append(nxt)

# 5. 출력
for i in range(1, N + 1):
    print(result[i])
