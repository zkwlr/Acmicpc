# G5

import sys

input = sys.stdin.readline


# 재귀 이해 핵심
# 맨 위의 함수에서 스택 프레임으로 들어가려고 하면 너무 어렵고 헷갈림
# 그냥 귀납적으로 base condition에서 성립하고,
# 정의된 함수와 그를 이용한 재귀 식을 통해 k일 때 해결 가능하면 k+1도 해결된다는게 명확하면
# 재귀는 성립한다.
# 1. base condition 설정과 2. 명확하고 깔끔한 함수 정의 3. 논리적인 재귀 방식
# 3가지를 구분하여 코드를 작성하자


# 1. 함수 정의 : a 에서 b로 n개의 원판을 옮기는 순서를 출력하는 함수
def hanoi(a, b, n):
    # 2. base condition n = 1
    if n == 1:
        print(f"{a} {b}")
        return

    # 3. 재귀 식(재귀 시스템)
    # n-1 개를 옮길 수 있으면 n개도 옮길 수 있으므로 귀납적으로 성립
    # a -> 출발지 b -> 목적지
    # n-1개의 원판을 목적지가 아닌 다른 장대로 옮기고 출력 (a -> 6-a-b)
    hanoi(a, 6 - a - b, n - 1)
    # n 원판을 목적지(b)로 옮기고 출력
    print(f"{a} {b}")
    # 다른 장대로 옮긴 n-1개의 원판을 목적지로 다시 이동 (6-a-b -> b)
    hanoi(6 - a - b, b, n - 1)


k = int(input())

# 총 횟수 = sigma(2k+1)
print(2**k - 1)
hanoi(1, 3, k)
