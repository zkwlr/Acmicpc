# B1

import sys

input = sys.stdin.readline

for i in range(3):
    a = input().rstrip()
    # input 중 숫자의 위치 확인(3개의 입력 중엔 숫자가 무조건 1개 있다)
    if a.isnumeric():
        ans = int(a) + 3 - i  # 숫자 위치에 따라 4번째 숫자 찾기
        break

if ans % 3 == 0 and ans % 5 == 0:
    print("FizzBuzz")
elif ans % 3 == 0:
    print("Fizz")
elif ans % 5 == 0:
    print("Buzz")
else:
    print(ans)
