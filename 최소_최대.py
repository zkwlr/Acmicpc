n = int(input())
min = 1000000
max = -1000000
nums = [int(x) for x in input().split()]
for i in range(n):
    a = nums[i]
    if a < min:
        min = a
    if a > max:
        max = a
print(min, max)
