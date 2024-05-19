# B2
n = int(input())

for i in range(n):
    a = input()
    streak = 0
    cnt = 0
    for chr in a:
        if chr == "O":
            streak += 1
            cnt += streak
        else:
            streak = 0
    print(cnt)
