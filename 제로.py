# S4
import sys

input = sys.stdin.readline

ls, k = [], int(input())

for _ in range(k):
    a = int(input())
    if a == 0:
        ls.pop()
    else:
        ls.append(a)

print(sum(ls[:]))
