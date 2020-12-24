import bisect

x = int(input())
num = list(map(int, input().split()))
num_idx = [num[0]]
dp = [0]

for n in num[1:]:
    if num_idx[-1] < n:
        num_idx.append(n)
        dp.append(len(num_idx) -1 )
    else:
        idx = bisect.bisect_left(num_idx, n)
        num_idx[idx] = n
        dp.append(idx)

length = len(num_idx)
print(length)
ans = []

for i in range(len(dp)-1, -1, -1):
    if dp[i] == length-1:
        ans.append(num[i])
        length -= 1

ans.reverse()
print(*ans)

# 시간초과를 어떻게 줄일 수 있지.. 고민을 다시 해봐야겠다.
# 메모리 154780KB 시간 1240ms
# how..