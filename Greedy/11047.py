x, total = map(int, input().split())

money = []
count = 0

for i in range(x):
    money.append(int(input()))

for i in range(x-1, -1, -1):
    if total == 0:
        break
    if total < money[i]:
        continue
    count += total // money[i]
    total %= money[i]

print(count)