x = int(input())

dp = [1 for i in range(x)]
child = []
for i in range(x):
    child.append(int(input()))

for i in range(x):
    for j in range(i):
        if child[i] > child[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(x - max(dp))

#  LIS
# 옮겨지는 아이의 최소 수 = 전체 수 - 옮기지 않아도 되는 아이의 수