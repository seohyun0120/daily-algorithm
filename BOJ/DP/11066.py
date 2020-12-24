# def solve():
#     N = int(input())
#     cost = list(map(int, input().split()))

#     table = [[0] * N for _ in range(N)]

#     for i in range(N-1):
#         table[i][i+1] = cost[i] + cost[i+1]
#         for j in range(i+2, N):
#             table[i][j] = table[i][j-1] + cost[j]
    
#     for d in range(2, N):
#         for i in range(N-d):
#             j = i+d
#             minim = [table[i][N] + table[N+1][j] for N in range(i, j)]
#             table[i][j] += min(minim)

#     print(table[0][N-1])

# x = int(input())
# for _ in range(x):
#     solve()