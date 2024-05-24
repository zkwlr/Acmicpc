# S5
import sys

input = sys.stdin.readline

ans, cnt = 1, 0
for i in range(1, int(input()) + 1):
    ans *= i

for i in str(ans)[::-1]:
    if i == "0":
        cnt += 1
    else:
        break

print(cnt)
