x = int(input())

number = list(map(int, input().split()))

stack = []
ans = [-1]*len(number)

for i, v in enumerate(number):
    while stack and v > number[stack[-1]]:
        last = stack.pop()
        ans[last] = v
    stack.append(i)

print(*ans)
