import bisect

x = int(input())
num = list(map(int, input().split()))

dp = [num[0]]

for i in range(x):
    if num[i] > dp[-1]:
        dp.append(num[i])
    else:
        idx = bisect.bisect_left(dp, num[i])
        dp[idx] = num[i]

print(len(dp))