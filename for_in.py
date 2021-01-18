n = int(input())

for i in range(n):
    if i % 3 == 0:
        continue
    if i == n:
        break
    print(i)
