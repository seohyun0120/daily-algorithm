x = int(input())
button = [300, 60, 10]
answer = []

if x % 10:
    print(-1)
else:
    for i in range(3):
        answer.append(x // button[i] )
        x %= button[i]
    print(*answer)