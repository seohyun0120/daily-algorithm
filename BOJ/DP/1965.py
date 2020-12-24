x = int(input())

box = list(map(int, input().split()))

dp = [1 for _ in range(x)]

for i in range(1, x):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# LIS(Longest Increasing Subsequence)라고도 한다고 한다..