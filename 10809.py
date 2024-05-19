# B2
from string import ascii_lowercase

alphabet_dict = {}
a = input()
for i in ascii_lowercase:
    alphabet_dict[i] = -1

for i in range(len(a)):
    if alphabet_dict[a[i]] != -1:
        continue
    else:
        alphabet_dict[a[i]] = i

for i in alphabet_dict.values():
    print(i, end="")
    print(" ", end="")
