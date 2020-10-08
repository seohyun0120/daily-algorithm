x = int(input())

count = 0

if x == 1 or x == 3:
    print(-1)

while x > 0:
    if x % 5 == 0:
        print(x // 5 + count)
        break
    count += 1
    x -= 2
