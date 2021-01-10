import sys
sys.setrecursionlimit(10 ** 5)

# 좌,우,상,하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    if check[x][y]:
        return check[x][y]

    check[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
            check[x][y] = max(check[x][y], dfs(nx,ny) + 1)

    return check[x][y]

n = int(input())
forest = []

for _ in range(n):
    forest.append(list(map(int, input().split())))

check = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        check[i][j] = dfs(i,j)

print(max(map(max, check)))