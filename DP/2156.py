x  = int(input())

p = []
for _ in range(x):
    p.append(int(input()))

dp = [0]
dp.append(p[0])

if (x>1):
    dp.append(p[0] + p[1])

for i in range(3, x+1):
    dp.append(max(
        p[i-1] + dp[i-2],
        p[i-1] + p[i-2] + dp[i-3],
        dp[i-1]
    ))

print(dp[x])