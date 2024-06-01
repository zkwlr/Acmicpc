# S2

import sys

input = sys.stdin.readline

ls, ans = [], []


n, m, b = map(int, input().split())
for i in range(n):
    x = input().rstrip().split()
    for i in x:
        ls.append(int(i))

ls.sort()

for h in range(ls[0], ls[-1] + 1):
    block, time = b, 0
    for i in ls:
        diff = i - h
        if diff:
            block += diff
            time += 2 * diff
        else:
            block -= diff
            time += diff

    if block < 0:
        continue
    else:
        ans.append([time, h])

ans.sort(key=lambda x: (x[0], -x[1]))
print(ans[0][0], ans[0][1])
