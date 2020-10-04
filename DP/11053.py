x = int(input())

case = list(map(int, input().split()))

dp = [0 for i in range(x+1)]

for i in range(x):
    dp[i] = 1
    for j in range(i):
        if case[i] > case[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))