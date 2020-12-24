n = int(input())

slime = list(map(int, input().split()))

slime.sort(reverse=True)

add = 0
total = 0
for i in range(1, n):
    add = slime[i-1] * slime[i]
    slime[i] = slime[i-1] + slime[i]
    total += + add

print(total)