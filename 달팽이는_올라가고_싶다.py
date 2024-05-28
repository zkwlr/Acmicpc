# B1

import sys
from math import *

input = sys.stdin.readline

a, b, v = map(int, input().split())

cnt = 1
v -= a  # 미리 마지막 a 연산을 시행

cnt += ceil(v / (a - b))

print(cnt)
