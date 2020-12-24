x = int(input())

t = []
p = []
dp = []

for i in range(x):
    input1, input2 = map(int, input().split())
    t.append(input1)
    p.append(input2)
    dp.append(input2)

dp.append(0)

for i in range(x-1, -1, -1):
    if t[i] + i > x:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])

print(dp[0])