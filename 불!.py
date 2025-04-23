# G3

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 탐색 기록 배열에서, 먼저 모든 칸을 -1로 두고, 벽은 0으로 설정해 접근할 필요 없게 하고
# 탐색 시작 지점도 0으로 설정하고 queue에 넣어두면
# dist가 0 이상인 부분은 이미 방문한 상태니 접근할 필요 없어 조건 형성에 간편

board = [input().rstrip() for _ in range(n)]

# 불 전파 기록용
fdist = [[-1] * m for _ in range(n)]

# 지훈이 탈출용
jdist = [[-1] * m for _ in range(n)]

jq = deque()
fq = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] == "#":
            fdist[i][j] = 0
            jdist[i][j] = 0
        if board[i][j] == "F":
            fq.append((i, j))
            fdist[i][j] = 0
        if board[i][j] == "J":
            jq.append((i, j))
            jdist[i][j] = 0


def fbfs():

    while fq:
        cur_x, cur_y = fq.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if fdist[nx][ny] >= 0:
                continue

            fdist[nx][ny] = fdist[cur_x][cur_y] + 1
            fq.append((nx, ny))


def jbfs():

    while jq:
        cur_x, cur_y = jq.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            # 경계를 넘어가면 그 순간 답
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return jdist[cur_x][cur_y] + 1
            # 벽이거나 이미 조사했으면 무시
            if jdist[nx][ny] >= 0:
                continue
            # 지훈이 시작점으로부터 거리가 불에서부터의 거리보다 더 크면 더 늦게 접근한 것이므로 탐색 필요 x
            # 현재 좌표 상하좌우 + 1 거리가 fdist에 기록된 값보다 같거나 크면
            # or 불이 접근하지 못한 칸이면 접근할 수 있게 해줘야함
            if fdist[nx][ny] != -1 and jdist[cur_x][cur_y] + 1 >= fdist[nx][ny]:
                # 조사할 필요 없음, 접근한 것만 표시
                jdist[nx][ny] = 0
                continue

            # 탈출 경로 조사 (큐에 넣음)
            jdist[nx][ny] = jdist[cur_x][cur_y] + 1
            jq.append((nx, ny))

    # jdist 가장자리를 조사해서 탈출 가능한지, 가능하면 최소 탈출 시간이 언제인지 확인
    # 0 이거나 -1 밖에 없으면 IMPOSSIBLE (벽이거나 가장자리에 접근하지 못함)
    ans = sys.maxsize
    for i in range(n):
        if i == 0 or i == n - 1:
            for j in range(m):
                if jdist[i][j] > 0:  # 기록된 거리가 외곽에 있으면
                    ans = min(ans, jdist[i][j])
        else:

            if jdist[i][0] > 0:
                ans = min(ans, jdist[i][0])
            if jdist[i][m - 1] > 0:
                ans = min(ans, jdist[i][m - 1])

    if ans == sys.maxsize:
        return "IMPOSSIBLE"
    else:
        return ans + 1


fbfs()
print(jbfs())
