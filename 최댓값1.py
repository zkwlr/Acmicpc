ans = 0
for i in range(9):
    a = int(input())

    if a > ans:
        ans = a
        index = i + 1
print(ans, index, sep="\n")
