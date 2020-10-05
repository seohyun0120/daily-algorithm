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

# 11053과 같은 문제지만 그렇게 풀면 시간초과를 경험하게 된다.
# loop를 돌 때, 현재까지의 부분 수열 max보다 더 클 경우, 부분 수열에 추가한다.
# 아닐 경우, 현재 위치만 업데이트
# 부분 수열 배열의 길이 출력