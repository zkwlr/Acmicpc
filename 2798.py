# B2
import sys
from itertools import *

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

ls = [int(x) for x in input().rstrip().split()]

set = list(combinations(ls, 3))
ans = 0

for i in set:
    if m - (i[0] + i[1] + i[2]) < 0:
        continue
    elif m - (i[0] + i[1] + i[2]) < m - ans:
        ans = i[0] + i[1] + i[2]

print(ans)
