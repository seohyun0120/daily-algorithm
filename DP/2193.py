x = int(input())

dp = [0 for i in range(91)]

dp[1] = 1 # 1
dp[2] = 1 # 10
dp[3] = 2  # 100 101
dp[4] = 3  # 1001 1000 1010

for i in range(4, x+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[x])