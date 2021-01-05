x = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1 for i in range(x)]
# decrease = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        # if reverse_case[i] > reverse_case[j]:
        #     decrease[i] = max(decrease[i], decrease[j]+1)

decrease2 = [1 for i in range(x)]
for i in range(x-1, -1, -1):
    for j in range(x-1, i, -1):
        if case[i] > case[j]:
            decrease2[i] = max(decrease2[i], decrease2[j]+1)

result = [0 for i in range(x)]
for i in range(x):
    # result[i] = increase[i] + decrease[x-i-1] -1 
    result[i] = increase[i] + decrease2[i] -1 

print(max(result))