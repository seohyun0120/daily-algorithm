x = int(input())
num = list(map(int, input().split()))

dp = [1] * x
arr = [[x] for x in num]

for i in range(x):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)

length = max(dp)
print(length)

max_idx = dp.index(length)
result = []

while max_idx >= 0:
    if dp[max_idx] == length:
        result.append(num[max_idx])
        length -= 1
    max_idx -= 1

result.reverse()
print(*result)

# 삽질을 좀 했다. 기존의 가장 긴 증가하는 부분 수열이랑 비슷할거라고 자만하고코드를 바꾸지않은 잘못
# 먼저, 가장 긴 증가 수열의 길이를 구하는 로직은 동일하다.
# dp의 최댓값이 있는 인덱스의 값부터 시작해서 거꾸로 탐색하며 새로운 배열을 만들고, reverse 시켜 출력하면 된다.
# 문제: 1 7 3 2 5 20 3
# dp:    1 2 2 2 3  4  3
# 20의 index부터 한칸씩 줄여가면서 배열을 채워나간다.