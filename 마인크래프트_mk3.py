# S2
# https://codingwonny.tistory.com/285
# 블록 위치당 높이를 기록하는게 아닌 높이를 index로 해서 높이당 블록의 개수를 기록(counting sort)
# 시간복잡도가 줄어드는 이유: 블록은 최대 500*500 = 250000개를 탐색해야 하지만
# 높이는 0~256으로 257개밖에 없기 떄문, 즉 범위가 작은 것을 index로 잡으면
# 시간복잡도를 크게 줄일 수 있다.

import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, b = map(int, input().split())

hcount = defaultdict(int)  # 어떤 높이를 가진 블록이 몇개 있는지
# 높이가 인덱스 (counting sort 방식)
ans = []
for _ in range(n):
    a = input().rstrip().split()
    for height in a:
        hcount[int(height)] += 1
# hcount = dict(sorted(hcount.items()))

for h in range(257):
    time, block = 0, b  # block: flatting 후 인벤토리 안의 최종 블록 수
    for height in hcount.keys():
        if height > h:
            block += hcount[height] * (
                height - h
            )  # 같은 높이를 가진 블록을 전부 한번에 처리
            time += 2 * hcount[height] * (height - h)
        else:
            block -= hcount[height] * (h - height)
            time += hcount[height] * (h - height)

    if block < 0:
        continue
    else:
        ans.append([time, h])
ans.sort(key=lambda x: (x[0], -x[1]))
print(ans[0][0], ans[0][1])
