# S3

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

adj = [[] for _ in range(n + 1)]

vis = [False] * (n + 1)

for _ in range(int(input())):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

q = deque()
q.append(1)
vis[1] = True
cnt = 0

while q:
    node = q.popleft()

    for neighbor in adj[node]:

        if vis[neighbor]:
            continue
        q.append(neighbor)
        vis[neighbor] = True
        # 감염된 컴퓨터 1개 증가
        cnt += 1

print(cnt)
