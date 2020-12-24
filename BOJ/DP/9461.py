x = int(input())

dp = [0 for i in range(101)]

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5]=  2

for _ in range(x):
    N = int(input())

    point = 1
    for i in range(6, N+1):
        dp[i] = dp[point] + dp[i-1]
        point += 1
    print(dp[N])