# B2

import sys
from string import ascii_lowercase

input = sys.stdin.readline

dic = {}
alpls = list(ascii_lowercase)
for i in range(len(alpls)):
    dic[alpls[i]] = i + 1
l = int(input())

ls = list(input().rstrip())

ans = 0
for i in range(len(ls)):
    ans += dic[ls[i]] * (31**i)

print(ans % 1234567891)
