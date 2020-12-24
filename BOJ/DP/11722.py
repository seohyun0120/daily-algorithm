x = int(input())

num = list(map(int, input().split()))

dp = [0 for i in range(x)]

for i in range(x):
    dp[i] = num[i]
    for j in range(i):
        if num[i] < num[j]:
            dp[i] = min(dp[i], dp[j] + 1)

print(min(dp))