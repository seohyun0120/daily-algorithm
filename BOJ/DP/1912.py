n = int(input())
numbers = list(map(int, input().split()))

dp = [0] * len(numbers)
dp[0] = numbers[0]

for i in range(1, len(numbers)):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])

dp.sort()
print(dp[-1])