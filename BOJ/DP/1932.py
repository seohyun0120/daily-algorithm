x = int(input())

p = []

for _ in range(x):
    p.append(list(map(int, input().split())))

k = 2

for i in range(1,x):
    for j in range(k):
        if j == 0:
            p[i][j] += p[i-1][j]
        elif i == j:
            p[i][j] += p[i-1][j-1]
        else:
            p[i][j] += max(p[i-1][j-1], p[i-1][j])
    k += 1

print(max(p[x-1]))
