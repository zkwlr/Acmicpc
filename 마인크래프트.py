# S2

import sys

input = sys.stdin.readline


def mine(x, y, ls):
    global block_in_case, time, h
    block_in_case += ls[x][y] - h
    time += 2 * (ls[x][y] - h)


def fill(x, y, ls):
    global block_in_case, time, h
    block_in_case -= h - ls[x][y]
    time += h - ls[x][y]


def flatting(ls, h):
    for i in range(n):
        for j in range(m):
            if ls[i][j] > h:
                mine(i, j, ls)
            elif ls[i][j] < h:
                fill(i, j, ls)


n, m, b = map(int, input().split())
ans = []

ls = [[int(x) for x in input().split()] for _ in range(n)]

# 1. 먼저 있는걸로 채워본다. n+1
# 1-1. 그럼, n층으로 고르게 해본다.
# 2. 안되면, 한층을 내려서 고르게 해보고 남은 부분 그 채운다. n-1
# 3. 안되면, 또 한층을 내려서 고르게 해보고 남은 부분 그 높이로 채운다. n-2
# 제일 높은블록부터 제일 낮은블록까지 높이를 정하고
# 그 높이까지 높은건 깎고 낮은건 채워서 채워지면 ans에 시간과 높이 추가
# 이후 시간 오름차순 정렬, 높이 내림차순 정렬


# max, min = 0, 257
# for i in ls:
#     for j in i:
#         if j > max:
#             max = j
#         if j < min:
#             min = j
mintime, maxheight = int(sys.maxsize), 0
for h in range(257):
    time, block_in_case = 0, b
    flatting(ls, h)

    if block_in_case < 0:
        continue
    else:
        # ans.append([time, h])
        if mintime >= time:
            mintime = time
            maxheight = h

# ans.sort(key=lambda x: (x[0], -x[1]))

# print(ans[0][0], ans[0][1])
print(mintime, maxheight)
# for i in ans:
#     print(i)
