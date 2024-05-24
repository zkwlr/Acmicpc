t = int(input())
for i in range(t):
    r, list = input().split()
    r = int(r)
    for j in range(len(list)):
        for k in range(r):
            print(list[j], end="")
    print()
