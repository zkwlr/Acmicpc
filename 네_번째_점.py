# B3

import sys

input = sys.stdin.readline

dic1 = {}
dic2 = {}
for _ in range(3):
    a, b = map(int, input().split())

    if a in dic1.keys():
        dic1[a] += 1
    else:
        dic1[a] = 1

    if b in dic2.keys():
        dic2[b] += 1
    else:
        dic2[b] = 1

# dic3 = {v: k for k, v in dic1.items()}
# dic4 = {v: k for k, v in dic2.items()}
# print(dic3[1], dic4[1])
print(
    [k for k, v in dic1.items() if v == 1][0], [k for k, v in dic2.items() if v == 1][0]
)
