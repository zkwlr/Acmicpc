# S3

import sys
from collections import defaultdict

input = sys.stdin.readline

ls, dic = [], defaultdict(int)
n = int(input())

for _ in range(n):
    a = int(input())
    ls.append(a)
    dic[a] += 1

sortedls = sorted(ls)
d2 = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(round(sum(ls) / n))
print(sortedls[n // 2])
if (
    len(d2) <= 1 or d2[0][1] != d2[1][1]
):  # 최빈값이 1개거나 길이가 1 이하인 경우 최빈값 출력
    print(d2[0][0])
else:  # 최빈값이 여러개면 두번째로 작은 값 출력
    print(d2[1][0])
print(sortedls[-1] - sortedls[0])
