# S2

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 간선 기록용
adj = [[] for _ in range(n + 1)]

# 그래프 생성
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 방문 기록 체크용(visited)
vis = [False] * (n + 1)


def bfs():
    cnt = 0
    for i in range(1, n + 1):
        # 방문한 적 있는 노드라면 스킵
        if vis[i]:
            continue
        # 방문한 적 없는 노드라면 connected components 개수 1개 증가시키고 queue에 넣고 기록하기
        queue = deque([i])
        vis[i] = True
        cnt += 1

        # queue가 빌 때까지 bfs 반복
        while queue:
            node = queue.popleft()
            # 이웃 노드에 대해 전부 방문 기록을 남기고 큐에 넣음
            for neighbor in adj[node]:
                if not vis[neighbor]:
                    queue.append(neighbor)
                    vis[neighbor] = True

    return cnt


print(bfs())
