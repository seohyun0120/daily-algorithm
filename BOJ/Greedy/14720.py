x = int(input())
store = list(map(int, input().split()))

milk = 0

for i in range(x):
    if(store[i] == milk % 3):
        milk += 1

print(milk)