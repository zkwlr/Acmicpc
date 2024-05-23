# B2
import sys

input = sys.stdin.readline

dic = {}
n = int(input())
for i in range(1, 1000001):
    idx = i
    for chr in str(i):
        idx += int(chr)
    if not idx in dic:
        dic[idx] = i

print(dic[n])
