x = input().split('-')
result = []

for i in x:
    count = 0
    s = i.split('+')
    for j in s:
        count += int(j)
    result.append(count)

ans = result[0]
for i in range(1, len(result)):
    ans -= result[i]

print(ans)