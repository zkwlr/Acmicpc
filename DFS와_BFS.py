import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, t = map(int, input().split())
    adj[u].append(t)
    adj[u].sort()
    adj[t].append(u)
    adj[t].sort()


def dfs(v):
    vis = [False] * (n + 1)
    stack = deque([v])

    while stack:
        # node를 스택에서 꺼내서 방문 후 출력
        node = stack.pop()
        # 꺼냈을 때 방문 기록
        if not vis[node]:
            vis[node] = True
            print(node, end=" ")

        # dfs에선 stack이기 때문에 작은 수부터 꺼내야 함
        # 주변 노드 스택에 삽입 후 방문 기록하기
        for neighbor in reversed(adj[node]):
            if not vis[neighbor]:
                stack.append(neighbor)
    print()


def bfs(v):
    vis = [False] * (n + 1)
    queue = deque([v])
    vis[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in adj[node]:
            if not vis[neighbor]:
                queue.append(neighbor)
                vis[neighbor] = True
    print()


dfs(v)
bfs(v)
