# B4
n = int(input())

for i in range(n):
    for j in range(n - 1 - i):
        print(" ", sep="", end="")
    for k in range(i + 1):
        print("*", sep="", end="")
    print()
