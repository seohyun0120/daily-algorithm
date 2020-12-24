x = int(input())

card = list(map(int, input().split()))
card = [0] + card

dp = [0 for i in range(x+1)]

dp[1] = card[1]
dp[2] = max(card[1] + card[1] , card[2])

# x번 카드 1개 or 1과 dp[x-1] or dp[2] 와 dp[n-2] ... 
for i in range(3, x+1):
    for j in range(i+1):
        dp[i] = max(dp[i], card[j] + dp[i-j])

print(dp[x])