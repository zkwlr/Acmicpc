# G5

import sys
from collections import deque

input = sys.stdin.readline

cnt = 0
is_first = True
ls = [deque() for _ in range(3)]
# 이동 순서 결과 저장용
q = deque()


def hanoi(n):
    # 첫 움직임 기록용
    global cnt, is_first, temp
    # base case n = 1
    if n == 1:
        for i in range(3):
            if ls[i][-1] == 1:
                # 처음 1의 움직임이고 n이 짝수라면
                # 2번째 칸으로 옮겨야 한다.
                if is_first:
                    is_first = False
                    if temp % 2 == 0:
                        cnt += 1
                        ls[1].append(ls[i].pop())
                        q.append(f"{i+1} 2")
                        return
                    else:  # n이 홀수라면 3번째 칸으로 옮겨야 한다.
                        cnt += 1
                        ls[2].append(ls[i].pop())
                        q.append(f"{i+1} 3")
                        return
                # 보통의 경우 1을 어디로 보내야 할지 정하기
                for j in range(3):
                    # 1. 먼저 2가 맨 위에 있다면 그쪽으로 보낸다.
                    if ls[j][-1] == 2:
                        cnt += 1
                        ls[j].append(ls[i].pop())
                        q.append(f"{i+1} {j+1}")
                        return
                a = 21
                aistrue = False
                for j in range(3):
                    # 2. 맨 위에 2가 없다면 남은 두 탑중 맨 위가 더 작은 짝수(or 0) 쪽으로 보내야 한다.
                    if j != i and ls[j][-1] % 2 == 0:
                        aistrue = True
                        if ls[j][-1] < a:
                            a = ls[j][-1]
                            aindex = j
                if aistrue:
                    cnt += 1
                    ls[aindex].append(ls[i].pop())
                    q.append(f"{i+1} {aindex+1}")
                    return

                # 3. 둘 다 홀수일때, 3이 없는 쪽으로 보낸다.
                for j in range(3):
                    if j != i and ls[j][-1] != 3:
                        cnt += 1
                        ls[j].append(ls[i].pop())
                        q.append(f"{i+1} {j+1}")
                        return

                # idea : 먼저 2가 있을 떈 2로 보내고,
                # 2가 없을땐 그냥 3이 없는 쪽으로만 보내면 되는 것 같은데?
                # 3도 없으면? 더 작은 짝수가 있는 곳으로..
                # 근데 그러면 3이 아예 없을 때 제대로 작동이 안됨

    # 먼저 목표한 탑을 옮기기 위해 n-1 하노이를 다른 쪽으로 옮긴다.
    hanoi(n - 1)

    # 부분적으로 맨 아래 칸을 옮기고 다시 n-1 하노이를 해서 남은 탑을 옮긴다.
    for i in range(3):
        if ls[i][-1] == n:
            for j in range(3):
                if ls[j][-1] >= n + 1:
                    ls[j].append(ls[i].pop())
                    cnt += 1
                    q.append(f"{i+1} {j+1}")
                    hanoi(n - 1)
                    return


n = int(input())
temp = n

# 맨 밑의 칸을 n+1로 가상으로 깐다.
for i in range(3):
    ls[i].append(n + 1)
# 하노이탑 생성
for i in reversed(range(n)):
    ls[0].append(i + 1)

hanoi(n)
print(cnt)
for i in q:
    print(i)

# 1번 판 움직임 알고리즘
# 처음 움직이는거면 n 짝수면 2번쨰, 홀수면 3번째
# 보통 때
# 2번 판이 있으면 1번 판을 2번 판쪽으로 옮겨야 하고
# 2번 판이 없으면 1번 판을 계속 짝수 칸에 보내야 한다.

# 둘 다 홀수면, 3이 없는 곳으로 보낸다.

# 처음에 1번을 둔 곳에 3탑이 세워진다.
