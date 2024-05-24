# B2
import sys

input = sys.stdin.readline

dic = {}
n = int(input())
for i in range(1, n + 1):
    idx = i
    for chr in str(i):
        idx += int(chr)
    if idx == n and (not idx in dic):
        dic[idx] = i

if n in dic:
    print(dic[n])
else:
    print(0)
