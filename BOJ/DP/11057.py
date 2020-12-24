x  = int(input())

num = [[0 for i in range(10)] for j in range(x)]
num[0] = [1 for i in range(10)]

for i in range(1, x):
    for j in range(10):
        for k in range(j, 10):
            num[i][k] += num[i-1][j]

print(sum(num[-1]) % 10007)

# 각 index로 끝날 수 있는 경우의 수 
# ex) 3자리수일 때, 3으로 끝날 수 있는 경우(6가지): 003 013 023 113 123 133 
# [1,1,1,1,1,1,1,1,1]
# [1,2,3,4,5,6,7,8,9,10]
# [1,3,6,10,15, 21, 28, 36, 45, 55]
