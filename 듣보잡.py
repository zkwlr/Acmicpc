# S4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ls1 = [input().rstrip() for _ in range(n)]
ls2 = [input().rstrip() for _ in range(m)]

dic = {}
for key in ls1:
    dic[key] = 0

for i in ls2:
    if i in dic.keys():
        dic[i] += 1

ans = [k for k, v in dic.items() if v == 1]
ans.sort()
print(len(ans))
for name in ans:
    print(name)
