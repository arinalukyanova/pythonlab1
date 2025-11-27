n = int(input())
tr, fl = 0, 0
for i in range(n):
    a, b, c, d = list(input().split())
    if d == "True":
        tr += 1
    else:
        fl += 1
print(tr, fl)
