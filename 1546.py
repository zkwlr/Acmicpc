# B1
sum = 0
n = int(input())
max = 0
list = [int(x) for x in input().split()]
for i in list:
    if max < i:
        max = i
for i in list:
    sum += i
sum = sum / max * 100 / n
print(sum)
