n, k = map(int, input().split())

coin = [int(input()) for i in range(n)]

dp = [0 for i in range(k+1)]
dp[0] = 1

for c in coin:
    for j in range(c, k+1):
        if j-c >= 0:
            dp[j] += dp[j-c]

print(dp[-1])
