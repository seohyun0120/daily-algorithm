import math
x = int(input())

dp = [0 for i in range(x+1)]

for i in range(x+1):
    dp[i] = i
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i], dp[i-j*j] + 1)
        j+= 1

print(dp[x]) 