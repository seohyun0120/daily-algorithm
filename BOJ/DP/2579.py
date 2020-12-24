x = int(input())

p = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(x):
    p[i] = int(input())

dp[0] = p[0]
dp[1] = p[0] + p[1]
dp[2] = max(p[0], p[1]) + p[2]

for i in range(3,x):
    dp[i] = max(dp[i-3] +p[i-1], dp[i-2]) + p[i]

print(dp[x-1])
