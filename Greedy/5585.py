x = int(input())

count = 0
change = 1000 - x

money = [500, 100, 50, 10, 5, 1]

for i in range(6):
    if change == 0:
        break
    if money[i] > change:
        continue
    count += change // money[i]
    change %= money[i]

print(count)