# B2

dic = {}
# dictionary는 key 중복 불가
for _ in range(10):
    dic[int(input()) % 42] = 1
print(len(dic))
