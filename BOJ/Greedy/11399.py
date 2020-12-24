x = int(input())

people = list(map(int, input().split()))
people.sort()

num = 0 

for i in range(x):
    for j in range(i+1):
        num += people[j]

print(num)