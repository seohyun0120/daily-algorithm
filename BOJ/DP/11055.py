x = int(input())

num = list(map(int, input().split()))

dp = [0 for i in range(x)]

for i in range(x):
    dp[i] = num[i]
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + num[i])

print(max(dp))

# 앞의 수보다 클 경우, 앞에서 나보다 작고, 길이가 긴 숫자 찾기