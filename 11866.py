# S5
import sys

# from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
ls = []
dic = {}
idx = 0
chk = 0
for i in range(n):
    dic[i] = 1

while 1:
    if chk == n:
        break
    cnt = 0
    while 1:
        if dic[idx % n] == 1 and cnt == k - 1:
            dic[idx % n] = 0
            ls.append((idx % n) + 1)
            idx = (idx + 1) % n
            chk += 1
            break
        elif dic[idx % n] == 1:
            cnt += 1
            idx = (idx + 1) % n
        elif dic[idx % n] == 0:
            idx = (idx + 1) % n

print("<", end="")
for i in range(len(ls) - 1):
    print(f"{ls[i]}, ", end="")
print(f"{ls[len(ls) - 1]}>")
