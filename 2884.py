# B3
h, m = map(int, (input().split()))
if m < 45:
    if h == 0:
        h = 23
    else:
        h -= 1
m = (m + 15) % 60
print(h, m)
