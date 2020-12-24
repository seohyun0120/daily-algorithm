x = int(input())
height = [-1] + list(map(int, input().split()))

result = [-1] * x

index = list(range(x))

for i in range(1, x+1):
    result[index.pop(height[i])] = i

print(*result)